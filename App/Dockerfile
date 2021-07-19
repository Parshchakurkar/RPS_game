#python version
FROM python

#Setting up working directory
WORKDIR /User/App/

#Copying file
COPY requirement.txt ./

#installing dependencies
RUN pip install -r requirement.txt

#Exposing to port
EXPOSE 5000

#need to check on copy command 
COPY RPS_Game.py .

#creating container
CMD [ "python","RPS_Game.py"]