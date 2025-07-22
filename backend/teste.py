import jwt

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTMyOTA0NjMsImlhdCI6MTc1MzIwNDA2Mywic3ViIjoiMSJ9.FH4G1TEm0xyjb4cWkXqVUCZwUFrsm-08LECMuutEba0"
key = "tech-solutio-secret-key-123"

try:
    payload = jwt.decode(token, key, algorithms=["HS256"])
    print("Válido ✅:", payload)
except Exception as e:
    print("Inválido ❌:", e)
