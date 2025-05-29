import json
import os
import asyncpg
import asyncio

async def handler(request):
    try:
        data = await request.json()
        username = data.get('username')
        password = data.get('password')
        phone = data.get('phone')
        smsCode = data.get('smsCode')
        company = data.get('company')
        sourcePage = data.get('sourcePage')

        conn = await asyncpg.connect(dsn=os.environ['DATABASE_URL'])
        await conn.execute(
            """
            INSERT INTO users (username, password, phone, sms_code, company, source_page)
            VALUES ($1, $2, $3, $4, $5, $6)
            """,
            username, password, phone, smsCode, company, sourcePage,
        )
        await conn.close()

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "注册成功"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
