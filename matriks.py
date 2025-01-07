def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def minor(matrix, row, col):
    return [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]

def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return determinant_2x2(matrix)
    det = 0
    for col in range(size):
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(minor(matrix, 0, col))
        det += cofactor
    return det

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))))
        result.append(row)
    return result

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Masukkan elemen baris {i+1} (pisahkan dengan spasi): ").split()))
        matrix.append(row)
    return matrix

def continue_or_exit():
    while True:
        choice = input("\nApakah Anda ingin melanjutkan? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Pilihan tidak valid, harap masukkan 'y' untuk ya atau 'n' untuk tidak.")

def main():
    print("Program untuk operasi matriks (penjumlahan, pengurangan, perkalian, transpose, determinan).")
    
    while True:
        num_matrices = int(input("Masukkan jumlah matriks yang ingin digunakan: "))
        matrices = []
        
        for m in range(num_matrices):
            print(f"\nMasukkan ukuran matriks {m+1}:")
            rows = int(input("Masukkan jumlah baris matriks: "))
            cols = int(input("Masukkan jumlah kolom matriks: "))
            print(f"\nMasukkan elemen-elemen matriks {m+1} ({rows}x{cols}):")
            matrix = input_matrix(rows, cols)
            matrices.append(matrix)
            print(f"\nMatriks {m+1} yang dimasukkan:")
            for row in matrix:
                print(" ".join(map(str, row)))
        
        print("\nPilih operasi matriks:")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Transpose Matriks")
        print("5. Determinan Matriks")
        operation = int(input("Masukkan pilihan (1-5): "))
        
        if operation == 1 or operation == 2:
            if num_matrices < 2:
                print("Anda perlu memasukkan minimal dua matriks untuk penjumlahan atau pengurangan.")
            else:
                result = matrices[0]
                for i in range(1, num_matrices):
                    if len(result) != len(matrices[i]) or len(result[0]) != len(matrices[i][0]):
                        print("Ukuran matriks tidak sama, penjumlahan atau pengurangan tidak dapat dilakukan.")
                        return
                    if operation == 1:
                        result = add_matrices(result, matrices[i])
                    elif operation == 2:
                        result = subtract_matrices(result, matrices[i])
                
                if operation == 1:
                    print("\nHasil Penjumlahan Matriks:")
                else:
                    print("\nHasil Pengurangan Matriks:")
                
                for row in result:
                    print(" ".join(map(str, row)))
        
        elif operation == 3:
            if num_matrices < 2:
                print("Anda perlu memasukkan minimal dua matriks untuk perkalian.")
            else:
                result = matrices[0]
                for i in range(1, num_matrices):
                    if len(result[0]) != len(matrices[i]):
                        print("Perkalian matriks tidak dapat dilakukan karena ukuran matriks tidak sesuai.")
                        return
                    result = multiply_matrices(result, matrices[i])
                
                print("\nHasil Perkalian Matriks:")
                for row in result:
                    print(" ".join(map(str, row)))
        
        elif operation == 4:
            result = transpose(matrices[0])
            print("\nHasil Transpose Matriks:")
            for row in result:
                print(" ".join(map(str, row)))
        
        elif operation == 5:
            if len(matrices[0]) != len(matrices[0][0]):
                print("Determinannya hanya dapat dihitung untuk matriks persegi.")
            else:
                det = determinant(matrices[0])
                print(f"\nDeterminannya adalah: {det}")
        
        else:
            print("\nPilihan tidak valid!")

        if not continue_or_exit():
            print("\nTerima kasih telah menggunakan program ini.")
            break

if __name__ == "__main__":
    main()
