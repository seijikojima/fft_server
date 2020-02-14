reference is https://github.com/maximemoreillon/img_to_json  
# Docker
docker build -t fft/serving .  
docker run -d fft/serving -p 5002:5002 fft/serving  

