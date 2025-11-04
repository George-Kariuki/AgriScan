import 'package:flutter_test/flutter_test.dart';
import 'package:agriscan/models/scan_result.dart';

void main() {
  group('ScanResult', () {
    test('stores data correctly', () {
      final result = ScanResult(
        imagePath: 'test.jpg',
        predictedClass: 'Cassava Mosaic Disease (CMD)',
        confidence: 0.92,
        timestamp: DateTime(2024, 1, 15, 10, 30),
        synced: true,
      );

      expect(result.imagePath, 'test.jpg');
      expect(result.predictedClass, 'Cassava Mosaic Disease (CMD)');
      expect(result.confidence, 0.92);
      expect(result.timestamp, DateTime(2024, 1, 15, 10, 30));
      expect(result.synced, true);
    });

    test('defaults to synced: false', () {
      final result = ScanResult(
        imagePath: 'test.jpg',
        predictedClass: 'Healthy',
        confidence: 0.85,
        timestamp: DateTime.now(),
      );

      expect(result.synced, false);
    });
  });
}

