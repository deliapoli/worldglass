# Montar archivos estáticos (solo si el directorio existe)
if os.path.isdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar templates
templates = Jinja2Templates(directory="templates")

# Importar rutas
from routes import chat, quotes, auth

app.include_router(chat.router, prefix="", tags=["chat"])
app.include_router(quotes.router, prefix="/api", tags=["quotes"])
app.include_router(auth.router, prefix="/api", tags=["auth"])

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Página principal con el chat"""
    return templates.TemplateResponse("chat.html", {"request": request})

@app.get("/health")
async def health():
    """Health check para Railway"""
    return {"status": "healthy", "service": "worldglass-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
