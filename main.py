import os 
from webapp import create_app

env = os.environ.get('WEBAPP_ENV' , 'dev')
print(env)
# app = create_app('config.%sConfig' %env.capitalize())

if __name__ == "__main__":
    app.run()