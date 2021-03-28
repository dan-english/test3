# Demo Center

### remove all old images
sudo docker system prune -a -f
sudo docker image prune -a -f

sudo docker build -t democenter  . 
sudo docker-compose build
sudo docker-compose up  --remove-orphans 

## when the container is running you may need to do the migrations (or if you need to run other craft commands) 
sudo docker-compose exec web craft migrate





# Environment Files
Docker copies `.env.docker` to `.env`
Locally you should `.env`
Heroku variables added via the Heroku dashboard
