import 'dart:io';
import 'package:flutter/material.dart';
import '../services/db_service.dart';

class HistoryScreen extends StatelessWidget {
  const HistoryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final results = DBService.getAllResults();

    return Scaffold(
      appBar: AppBar(title: const Text('Scan History')),
      body: results.isEmpty
          ? const Center(child: Text('No scans yet'))
          : ListView.builder(
              itemCount: results.length,
              itemBuilder: (context, i) {
                final r = results[i];
                return ListTile(
                  leading: ClipRRect(
                    borderRadius: BorderRadius.circular(8),
                    child: Image.file(
                      File(r.imagePath),
                      width: 56,
                      height: 56,
                      fit: BoxFit.cover,
                      errorBuilder: (context, error, stackTrace) {
                        return Container(
                          width: 56,
                          height: 56,
                          color: Colors.grey[300],
                          child: const Icon(Icons.image_not_supported),
                        );
                      },
                    ),
                  ),
                  title: Text(r.predictedClass),
                  subtitle: Text(
                    'Confidence: ${(r.confidence * 100).toStringAsFixed(1)}% • ${_formatDate(r.timestamp)}',
                  ),
                  trailing: Icon(
                    r.synced ? Icons.cloud_done : Icons.cloud_off,
                    color: r.synced ? Colors.green : Colors.grey,
                  ),
                );
              },
            ),
    );
  }

  String _formatDate(DateTime date) {
    return '${date.day}/${date.month}/${date.year} ${date.hour}:${date.minute.toString().padLeft(2, '0')}';
  }
}

