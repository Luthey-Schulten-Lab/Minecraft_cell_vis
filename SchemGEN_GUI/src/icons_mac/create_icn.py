from PIL import Image
import os

def create_icns(png_path, icns_path):
    # Open the PNG image
    img = Image.open(png_path)

    # Ensure the image is square
    size = max(img.size)
    img = img.resize((size, size), Image.LANCZOS)

    # Create a new ICNS file
    with open(icns_path, 'wb') as icns_file:
        # Write the ICNS header
        icns_file.write(b'icns')
        icns_file.write(b'\x00' * 4)  # Placeholder for total size

        sizes = [1024, 512, 256, 128, 64, 32, 16]
        for size in sizes:
            # Resize the image
            resized = img.resize((size, size), Image.LANCZOS)
            
            # Convert to RGBA if not already
            if resized.mode != 'RGBA':
                resized = resized.convert('RGBA')

            # Prepare the icon data
            icon_data = resized.tobytes()

            # Write the icon header
            if size >= 256:
                icns_file.write(b'ic' + bytes([size // 100 + 48, size % 100 // 10 + 48]))
            else:
                icns_file.write(b'ic' + bytes([size // 10 + 48, size % 10 + 48]))
            
            icns_file.write(len(icon_data).to_bytes(4, byteorder='big'))
            
            # Write the icon data
            icns_file.write(icon_data)

        # Go back and write the total file size
        total_size = icns_file.tell()
        icns_file.seek(4)
        icns_file.write(total_size.to_bytes(4, byteorder='big'))

    print(f"ICNS file created: {icns_path}")

# Usage
png_path = 'software_icon.png'
icns_path = 'software_icon.icns'
create_icns(png_path, icns_path)