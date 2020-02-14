reference is https://github.com/maximemoreillon/img_to_json  
# Docker
docker build -t sig2spec .  
docker run -d fft/serving -p 5002:5002 sig2spec 

