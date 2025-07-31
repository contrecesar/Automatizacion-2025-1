- Python 3.10 o superior
  
Primero es lo mas recomendable crear uun ambiente virtual para no tener ningun problema 
  py -m venv .venv

.venv\Scripts\activate

Luego instalariamos todas las dependencias necesarias, se puede gracias al documento de requirements

pip install -r requirements.txt

o si se quiere instalar manualmente

pip install transformers datasets scikit-learn torch torchvision torchaudio numpy
pip install "accelerate>=0.26.0"
pip install "transformers[torch]"

para poder iniciar el proyecto es necesario hacerlo con el primero archivo
python finetune.py

Creara carpetas adicionales con toda la data necesaria al hacer el training
python test_model.py
