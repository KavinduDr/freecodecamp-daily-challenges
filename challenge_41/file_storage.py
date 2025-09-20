def number_of_files(file_size, file_unit, drive_size_gb):
    """
    Calculate the number of files that can fit on a drive.

    :param file_size: Size of the file (float or int).
    :param file_unit: Unit of the file size ('B', 'KB', 'MB', 'GB').
    :param drive_size_gb: Size of the drive in gigabytes (float or int).
    :return: Number of files that can fit on the drive (int).
    """

    # Define conversion factors to bytes
    unit_factors = {
        'B': 1,
        'KB': 1000,
        'MB': 1000**2,
        'GB': 1000**3
    }

    #convert file size into bytes
    file_size_in_bytes = file_size * unit_factors[file_unit]
    # convert drive size into bytes
    drive_size_in_bytes = drive_size_gb * unit_factors['GB']

    # calculate number of files can be fitted
    num_files = drive_size_in_bytes // file_size_in_bytes
    return int(num_files)

# Example usage
file_size = 500
file_unit = 'KB'
drive_size_gb = 2
print(number_of_files(file_size, file_unit, drive_size_gb))  # Output: