"""Performance tests for Bank Marketing Prediction API - No external dependencies"""
import time
import statistics
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

# Sample valid customer data for testing
VALID_CUSTOMER = {
    "age": 35,
    "job": "management",
    "marital": "married",
    "education": "university.degree",
    "default": "no",
    "balance": 2500,
    "housing": "yes",
    "loan": "no",
    "contact": "cellular",
    "day": 15,
    "month": "may",
    "campaign": 1,
    "pdays": -1,
    "previous": 0,
    "poutcome": "unknown"
}

class TestPerformance:
    """Performance test cases using TestClient (no external API needed)"""
    
    def test_response_time_local(self):
        """Test API response time on local machine using TestClient"""
        times = []
        
        print("\n🔄 Running 100 requests...")
        for i in range(100):
            start = time.time()
            response = client.post("/predict", json=VALID_CUSTOMER)
            elapsed = time.time() - start
            times.append(elapsed)
            
            # Ensure all requests succeeded
            assert response.status_code == 200
            
            if (i + 1) % 20 == 0:
                print(f"   Completed {i + 1}/100 requests")
        
        # Calculate statistics
        avg_time = statistics.mean(times) * 1000  # Convert to milliseconds
        max_time = max(times) * 1000
        min_time = min(times) * 1000
        
        # Calculate 95th percentile
        sorted_times = sorted(times)
        p95_index = int(len(sorted_times) * 0.95)
        p95_time = sorted_times[p95_index] * 1000
        
        # Print results
        print(f"\n📊 Performance Test Results:")
        print(f"   Average time: {avg_time:.2f} ms")
        print(f"   Min time: {min_time:.2f} ms")
        print(f"   Max time: {max_time:.2f} ms")
        print(f"   95th percentile: {p95_time:.2f} ms")
        
        # Assertions (fail if too slow)
        assert avg_time < 500, f"Average time {avg_time:.2f}ms exceeds 500ms"
        assert p95_time < 1000, f"95th percentile {p95_time:.2f}ms exceeds 1000ms"
        
        print("\n✅ Performance test PASSED!")
    
    def test_response_time_under_load(self):
        """Test API response time under simulated concurrent load"""
        import concurrent.futures
        
        def make_request():
            start = time.time()
            response = client.post("/predict", json=VALID_CUSTOMER)
            return time.time() - start
        
        print("\n🔄 Running 50 concurrent requests...")
        
        # Make 50 concurrent requests using 10 workers
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(50)]
            times = [f.result() for f in futures]
        
        avg_time = statistics.mean(times) * 1000
        max_time = max(times) * 1000
        
        print(f"\n📊 Load Test Results (50 concurrent requests):")
        print(f"   Average time: {avg_time:.2f} ms")
        print(f"   Max time: {max_time:.2f} ms")
        
        assert avg_time < 1000, f"Load test avg {avg_time:.2f}ms exceeds 1000ms"
        
        print("\n✅ Load test PASSED!")

# Optional: Run standalone
if __name__ == "__main__":
    test = TestPerformance()
    test.test_response_time_local()
    test.test_response_time_under_load()