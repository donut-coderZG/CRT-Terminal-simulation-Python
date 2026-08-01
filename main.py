import time
import random
import getpass

def glitch_print(message, delay=0.04):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def realistic_loading(target_duration=55):
    progress = 0
    start_time = time.time()
    
    # Scale progress increments dynamically to hit the target duration smoothly
    while progress < 100:
        elapsed = time.time() - start_time
        expected_progress = (elapsed / target_duration) * 100
        
        # Add slight random fluctuation so the bar moves realistically
        flg = random.choice([1, 1, 2, 0, -1]) if progress < 95 else 0
        progress = max(0, min(100, int(expected_progress) + flg))
        
        if progress >= 100:
            break
            
        width = 30
        filled = int(width * (progress / 100))
        bar = "█" * filled + "░" * (width - filled)
        
        status = "CONNECTING"
        if progress > 30: status = "HANDSHAKING"
        if progress > 60: status = "DOWNLOADING"
        if progress > 90: status = "VERIFYING"
        
        print(f"\r\033[92m[ {bar} ] {progress}% {status}...", end="", flush=True)
        time.sleep(random.uniform(0.04, 0.08))
        
    print("\r\033[92m[ ██████████████████████████████ ] 100% COMPLETE...   ", end="", flush=True)
    print("\n")

def matrix_rain(duration=25):
    cpp_snippets = [
        "int* ptr = new int;", "std::cout << kernel_panic << std::endl;",
        "void* mem = malloc(sizeof(char) * 256);", "template <typename T> class Matrix { };",
        "#include <iostream>", "virtual uint32_t get_address() const;",
        "for(int i = 0; i < stack_limit; ++i)", "if (system_integrity == 0x0) break;",
        "asm { mov eax, 1; int 0x80; }", "std::vector<std::string> buffer;"
    ]
    for _ in range(duration):
        line = random.choice(cpp_snippets)
        padding = " " * random.randint(0, 30)
        print(f"\033[32m{padding}{line}\033[0m")
        time.sleep(0.08)

def decrypt_effect(target_list):
    chars = "0123456789"
    for item in target_list:
        print("  ", end="")
        for _ in range(5):
            print(random.choice(chars), end="", flush=True)
            time.sleep(0.01)
            print("\b", end="", flush=True)
        print(item, end=" ", flush=True)
        time.sleep(0.02)
    print()

js_snippets = [
    "const data = await fetch('/api/v1/db/vault');", "document.getElementById('security-grid').innerHTML = '';",
    "if (user.clearanceLevel < 10) { throw new Error('Forbidden'); }", "localStorage.setItem('session_token', 'dGhlX3Bhc3N3b3Jk');",
    "export default function decrypt(hash, salt) { return Buffer.from(hash); }", "process.env.DB_PASSWORD = Buffer.alloc(16, Math.random());",
    "window.crypto.subtle.generateKey({name: 'AES-GCM', length: 256});", "Object.freeze(systemCore.protocols);",
    "console.log(`Connected to: ${socket.address().ip}`);", "setTimeout(() => { bypassFirewall(0x8821); }, 500);"
]

raw_numbers = "9012915492879345941095669632970198899924904391229250937894999505968897149831995090779191920493339462952996559780981799989005913892619394942795839619974698609903"
admin_list = [raw_numbers[i:i+4] for i in range(0, len(raw_numbers), 4)]

print("\033[32m")
matrix_rain(25)
glitch_print(">>> SYSTEM FILE DOWNLOAD COMPLETE")
time.sleep(1)

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    glitch_print(f"\n[ NODE_{random.randint(100,999)} ]")
    raw_input = getpass.getpass("ENTER ACCESS CODE: ")
    print("*" * len(raw_input))
    
    if raw_input == "9330":
        glitch_print(">>> ROOT AUTHENTICATION DETECTED.")
        secondary_input = getpass.getpass("ENTER MASTER KEY: ")
        print("*" * len(secondary_input))
        if secondary_input == "9171":
            glitch_print(">>> ESTABLISHING INTERNET CONNECTION 10 MEGABIT CONNECTING...")
            random_duration = random.randint(45, 65)
            realistic_loading(random_duration)
            glitch_print(">>> BREAKING ENCRYPTION...")
            time.sleep(0.5)
            for _ in range(30):
                prefix = f" {random.choice(['>>', '<<', '=='])} "
                code_line = random.choice(js_snippets)
                print(f"\033[92m{prefix}{code_line}\033[0m")
                time.sleep(0.04)
            glitch_print("\n>>> FILE DOWNLOAD COMPLETE.")
            glitch_print(">>> DECRYPTING AUTHORIZED ID LIST...")
            for i in range(0, len(admin_list), 4):
                decrypt_effect(admin_list[i:i+4])
            break
        else:
            glitch_print(">>> MASTER KEY INVALID.")
            attempts += 1
    elif raw_input == "9156":
        glitch_print(">>> GUEST BYPASS ENABLED.")
        glitch_print(">>> ESTABLISHING INTERNET CONNECTION 10 MEGABIT CONNECTING...")
        random_duration = random.randint(45, 65)
        realistic_loading(random_duration)
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            glitch_print(">>> TRACE DETECTED... REROUTING...")
            time.sleep(1)
        else:
            glitch_print(">>> SYSTEM CRASH.")
            for _ in range(100):
                print(random.choice("01"), end="", flush=True)
                time.sleep(0.01)
            print("\n>>> SIGNAL LOST.")

print("\033[0m")
