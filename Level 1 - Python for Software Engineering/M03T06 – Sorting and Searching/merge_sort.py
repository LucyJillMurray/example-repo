def merge_sort(items):
    # Get the length of the input list
    items_length = len(items)

    # Create temporary storage for merging
    temporary_storage = [None] * items_length

    # Initialise the size of subsections to 1
    size_of_subsections = 1

    # Iterate until the size of subsections is less than the length of the list
    while size_of_subsections < items_length:

        # Iterate over the list in steps of size_of_subsections * 2
        for i in range(0, items_length, size_of_subsections * 2):

            # Determine the start and end indices of the first subsection
            first_section_start = i
            first_section_end = min(i + size_of_subsections, items_length)

            # Determine the start and end indices of the second subsection
            second_section_start = first_section_end
            second_section_end = min(
                first_section_end + size_of_subsections, items_length
            )

            # Define the sections to merge
            sections = (
                (first_section_start, first_section_end),
                (second_section_start, second_section_end),
            )

            # Call the merge function to merge the subsections
            merge(items, sections, temporary_storage)

        # Double the size of subsections for the next iteration
        size_of_subsections *= 2

    # Return the sorted list
    return items


def merge(items, sections, temporary_storage):
    # Unpack the sections tuple to get the start and end indices
    # of each section.
    (first_section_start, first_section_end), (
        second_section_start,
        second_section_end,
    ) = sections

    # Initialise indices for the two sections and temporary storage
    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    # Loop until both sections have been fully merged
    while left_index < first_section_end or right_index < second_section_end:

        # Check if both sections still have elements to compare
        if left_index < first_section_end and right_index < second_section_end:

            # Compare elements from both sections
            if len(items[left_index]) > len(items[right_index]):
                # Place the longer string into temporary storage
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
            else:
                # len(items[right_index]) >= len(items[left_index])
                temporary_storage[temp_index] = items[right_index]
                right_index += 1

            temp_index += 1

        # If section 1 still has elements left to merge
        elif left_index < first_section_end:
            # Copy remaining elements from section 1 to temporary storage
            for i in range(left_index, first_section_end):
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1

        # If section 2 still has elements left to merge
        else:
            # right_index < second_section_end
            # Copy remaining elements from section 2 to temporary storage
            for i in range(right_index, second_section_end):
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1

    # Copy sorted elements from temporary storage back to the original list
    for i in range(temp_index):
        items[first_section_start + i] = temporary_storage[i]


example_list1 = [
    "shorter",
    "s",
    "very very long",
    "short",
    "sho",
    "very long",
    "so",
    "so so",
    "exceptionally long",
    "shortish",
]
example_list2 = [
    "sun",
    "elephant",
    "a",
    "computer",
    "dog",
    "blueberry",
    "hi",
    "mountain",
    "tree",
    "encyclopedia",
    "go",
    "pencil",
]
example_list3 = [
    "apple",
    "I",
    "sunshine",
    "car",
    "butterfly",
    "no",
    "mount",
    "zebra",
    "algorithm",
    "to",
]
sorted_list1 = merge_sort(example_list1)
print(sorted_list1)

sorted_list2 = merge_sort(example_list2)
print(sorted_list2)

sorted_list3 = merge_sort(example_list3)
print(sorted_list3)
