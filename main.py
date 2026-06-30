from fastapi.responses import JSONResponse

@app.post("/verify")
def verify(req: TokenRequest):
    try:
        payload = jwt.decode(
            req.token,
            PUBLIC_KEY,
            algorithms=["RS256"],
            issuer=ISSUER,
            audience=AUDIENCE,
        )

        return JSONResponse(
            status_code=200,
            content={
                "valid": True,
                "email": payload["email"],
                "sub": payload["sub"],
                "aud": payload["aud"],
            },
        )

    except Exception:
        return JSONResponse(
            status_code=401,
            content={"valid": False},
        )