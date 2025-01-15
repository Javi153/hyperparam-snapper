from prediction import model_prediction

from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}
	
@app.post("/predict")
def predict(X: UploadFile):
	content = eval(X.file.read())
	result = model_prediction(content)
	response = "Para los datos obtenidos tenemos los siguientes resultados: \n"
	for i in range(len(result)):
		response += "Consulta %i: %s\n" % (i, result[i])
	return response
	
