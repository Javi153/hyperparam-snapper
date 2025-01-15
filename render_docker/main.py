from prediction import model_prediction

from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse('index.html')
	
@app.post("/predict", response_class=HTMLResponse)
async def predict(file: UploadFile):
	content = eval(file.file.read())
	result = model_prediction(content)
	response = """<!DOCTYPE html>
	<html>
	<body><p>Para los datos obtenidos tenemos los siguientes resultados:</p>"""
	for i in range(len(result)):
		response += "<p>Consulta %i: %s</p>" % (i+1, result[i])
	response += """</body>
	</html>"""
	return response
