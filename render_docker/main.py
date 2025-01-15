from prediction import model_prediction

from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse('index.html')
	
@app.post("/predict", response_class=HTMLResponse)
async def predict(X: UploadFile):
	content = eval(X.file.read())
	result = model_prediction(content)
	response = """<!DOCTYPE html>
	<html>
	<body>Para los datos obtenidos tenemos los siguientes resultados: \n"""
	for i in range(len(result)):
		response += "Consulta %i: %s\n" % (i, result[i])
	response += response + """</body>
	</html>"""
	return response
