@echo "Starting billing service"
cd billing_svc/
python app.py &

@echo "Starting inventory service"
cd ../inventory_svc/
python app.py &

@echo "Starting shipping service"
cd ../shipping_svc/
python app.py &
