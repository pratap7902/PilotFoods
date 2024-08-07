from django_rq import job
@job
def send_email_task(order_id):
    print(f"Sending Email for Order ID: {order_id}")