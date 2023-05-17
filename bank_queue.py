import random
import time


class Customer:
    def __init__(self, name, transaction_time):
        self.name = name
        self.transaction_time = transaction_time
        self.entered_queue_time = 0
        self.left_queue_time = 0


class BankQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)


class BankSimulation:
    def __init__(self, num_customers, service_time_mean):
        self.customers = []
        self.bank_queue = BankQueue()
        self.num_customers = num_customers
        self.service_time_mean = service_time_mean

    def generate_customers(self):
        for i in range(self.num_customers):
            customer = Customer(
                f"Pelanggan {i+1}", random.expovariate(1/self.service_time_mean))
            self.customers.append(customer)

    def run_simulation(self):
        self.generate_customers()
        for customer in self.customers:
            print(f"{customer.name} masuk antrian pada {time.time()}")
            customer.entered_queue_time = time.time()
            self.bank_queue.enqueue(customer)

        while not self.bank_queue.is_empty():
            customer = self.bank_queue.dequeue()
            print(f"{customer.name} keluar antrian pada {time.time()}")
            customer.left_queue_time = time.time()
            time_in_queue = customer.left_queue_time - customer.entered_queue_time
            print(
                f"{customer.name} menghabiskan {time_in_queue:.2f} detik dalam antrian")

            service_time = random.expovariate(1/self.service_time_mean)
            print(f"{customer.name} dilayani selama {service_time:.2f} detik")
            time.sleep(service_time)

            print(f"{customer.name} selesai transaksi pada {time.time()}")


if __name__ == "__main__":
    sim = BankSimulation(num_customers=10, service_time_mean=5)
    sim.run_simulation()
