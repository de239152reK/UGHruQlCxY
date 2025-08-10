# 代码生成时间: 2025-08-10 21:46:56
import hashlib
import numpy as np
def calculate_hash(data, algorithm='sha256', as_np_array=False):
    """
# NOTE: 重要实现细节
    Calculate the hash of the input data using the specified algorithm.
    
    Parameters:
    - data (str, bytes or numpy.ndarray): The data to calculate the hash for.
    - algorithm (str): The hash algorithm to use. Default is 'sha256'.
    - as_np_array (bool): If True, return the hash as a numpy array. Default is False.
    
    Returns:
    - hash_value (str or numpy.ndarray): The calculated hash value.
    
    Raises:
    - ValueError: If the algorithm is not supported.
    """
# TODO: 优化性能
    # Check if the algorithm is supported
# 改进用户体验
    supported_algorithms = {'md5', 'sha1', 'sha256', 'sha512'}
    if algorithm not in supported_algorithms:
        raise ValueError(f"Unsupported algorithm: {algorithm}. Supported algorithms are: {supported_algorithms}")
    
    # Convert data to bytes if it's a string or numpy array
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif isinstance(data, np.ndarray):
        data = data.tobytes()
    
    # Calculate the hash
    hash_object = hashlib.new(algorithm, data)
    hash_value = hash_object.hexdigest()
    
    # Return the hash as a numpy array if requested
    if as_np_array:
# 添加错误处理
        hash_value = np.array(list(hash_value), dtype=np.uint8)
    
    return hash_value
def main():
    # Example usage
    data = 'Hello, World!'
    hash_result = calculate_hash(data, 'sha256')
    print(f"Hash of '{data}' using SHA-256: {hash_result}")
# 添加错误处理
    
    # Example usage with numpy array
# 优化算法效率
    data_array = np.array([1, 2, 3, 4, 5])
    hash_result_array = calculate_hash(data_array, 'sha256', as_np_array=True)
    print(f"Hash of array {data_array} using SHA-256: {hash_result_array}")
    
if __name__ == '__main__':
    main()