import heapq
import tempfile
import os

def external_merge_sort(input_file, output_file, chunk_size=1000000):
    chunks = []

    # STEP 1: Read file in chunks, sort, write to temp files
    with open(input_file, 'r') as f:
        chunk = []

        for line in f:
            chunk.append(int(line.strip()))

            if len(chunk) == chunk_size:
                chunk.sort()

                temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
                for item in chunk:
                    temp_file.write(f"{item}\n")
                temp_file.close()

                chunks.append(temp_file.name)
                chunk = []

        # remaining elements (last chunk)
        if chunk:
            chunk.sort()
            temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
            for item in chunk:
                temp_file.write(f"{item}\n")
            temp_file.close()
            chunks.append(temp_file.name)

    # STEP 2: Merge all sorted temp files using heap
    with open(output_file, 'w') as out:
        heap = []
        files = [open(chunk, 'r') for chunk in chunks]

        # push first element of each file into heap
        for i, f in enumerate(files):
            line = f.readline()
            if line:
                heapq.heappush(heap, (int(line.strip()), i))

        # extract min and push next from same file
        while heap:
            val, i = heapq.heappop(heap)
            out.write(f"{val}\n")

            line = files[i].readline()
            if line:
                heapq.heappush(heap, (int(line.strip()), i))

        # close files
        for f in files:
            f.close()

    # STEP 3: delete temp files
    for chunk in chunks:
        os.unlink(chunk)


# Usage
external_merge_sort('large_unsorted_file.txt', 'sorted_output.txt')
