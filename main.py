import time # Bo dem thoi gian chay
import random # Bo tao so ngau nhien

# ============================================================
# PHAN 1: THUAT TOAN TIM KIEM (SEARCHING)
# ============================================================

def linear_search(arr, x):
    """Thuat toan tim kiem tuyen tinh"""
    # Buoc 1: Duyet qua tung phan tu cua danh sach
    for i in range(len(arr)):
        # Buoc 2: Neu tim thay x thi tra ve vi tri i
        if arr[i] == x:
            return i
    return -1  # Khong tim thay

def binary_search(arr, x):
    """Thuat toan tim kiem nhi phan (yeu cau mang da sap xep)"""
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Buoc 1: Lay vi tri o giua
        mid = (left + right) // 2
        
        # Buoc 2: So sanh phan tu giua voi x
        if arr[mid] == x:
            return mid       # Tim thay
        elif arr[mid] < x:
            left = mid + 1   # Tim o nua ben phai
        else:
            right = mid - 1  # Tim o nua ben trai
            
    return -1 # Khong tim thay

# ============================================================
# PHAN 2: THUAT TOAN SAP XEP (SORTING)
# ============================================================

def bubble_sort(arr):
    """Sap xep noi bot: Day phan tu lon nhat ve cuoi"""
    n = len(arr)
    # Copy mang de khong lam hong du lieu goc khi demo
    arr_new = arr.copy() 
    
    for i in range(n):
        # Buoc 1: Duyet cac phan tu chua sap xep
        for j in range(0, n - i - 1):
            # Buoc 2: Neu phan tu truoc lon hon phan tu sau -> Doi cho
            if arr_new[j] > arr_new[j + 1]:
                arr_new[j], arr_new[j + 1] = arr_new[j + 1], arr_new[j]
                
    return arr_new

def insertion_sort(arr):
    """Sap xep chen: Chen phan tu vao dung vi tri da sap xep"""
    arr_new = arr.copy()
    
    for i in range(1, len(arr_new)):
        key = arr_new[i]
        j = i - 1
        
        # Buoc 1: Doi cac so lon hon 'key' ra sau
        while j >= 0 and key < arr_new[j]:
            arr_new[j + 1] = arr_new[j]
            j -= 1
        
        # Buoc 2: Chen 'key' vao cho trong
        arr_new[j + 1] = key
        
    return arr_new

# ============================================================
# PHAN 3: SO HOC (GCD - EUCLID)
# ============================================================

def gcd_euclidean(a, b):
    """Tim Uoc chung lon nhat (UCLN) bang thuat toan Euclid"""
    while b != 0:
        # Gan a bang b, va b bang phan du a chia b
        a, b = b, a % b
    return a

# ============================================================
# PHAN 4: CHUONG TRINH CHINH (MAIN)
# ============================================================

def measure_time(name, func, *args):
    """Ham do thoi gian chay va in ket qua"""
    start = time.time()       # Bam gio
    result = func(*args)      # Chay thuat toan
    end = time.time()         # Dung gio
    
    print(f"[{name}]")
    # In ket qua ngan gon neu no qua dai
    res_str = str(result)
    if len(res_str) > 50:
        print(f" -> Ket qua: {res_str[:50]}...") 
    else:
        print(f" -> Ket qua: {res_str}")
        
    print(f" -> Thoi gian: {(end - start) * 1000:.4f} ms") # Doi sang mili giay
    print("-" * 30)

if __name__ == "__main__":
    # --- Tao du lieu mau ---
    print("=== TAO DU LIEU MAU ===")
    n = 2000 # So luong phan tu
    data = [random.randint(1, 10000) for _ in range(n)]
    target = data[random.randint(0, n-1)] # Chon bua 1 so de tim
    
    print(f"Mang ngau nhien {n} phan tu.")
    print(f"So can tim: {target}\n")

    # --- Demo Tim kiem ---
    print("=== 1. DEMO TIM KIEM ===")
    measure_time("Tim kiem tuyen tinh (Linear Search)", linear_search, data, target)
    
    # Binary search can mang da sap xep
    data_sorted = sorted(data)
    measure_time("Tim kiem nhi phan (Binary Search)", binary_search, data_sorted, target)

    # --- Demo Sap xep ---
    print("\n=== 2. DEMO SAP XEP ===")
    # Dung mang nho hon de demo sap xep (vi O(n^2) chay lau)
    small_data = [random.randint(1, 1000) for _ in range(500)]
    
    measure_time("Sap xep noi bot (Bubble Sort)", bubble_sort, small_data)
    measure_time("Sap xep chen (Insertion Sort)", insertion_sort, small_data)

    # --- Demo So hoc ---
    print("\n=== 3. DEMO UCLN (EUCLID) ===")
    measure_time("UCLN cua 270 va 192", gcd_euclidean, 270, 192)