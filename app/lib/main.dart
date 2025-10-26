import 'package:flutter/material.dart';

void main() {
  runApp(const AgriScanApp());
}

class AgriScanApp extends StatelessWidget {
  const AgriScanApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AgriScan',
      home: Scaffold(
        appBar: AppBar(title: const Text('AgriScan')),
        body: const Center(child: Text('Welcome to AgriScan')),
      ),
    );
  }
}
