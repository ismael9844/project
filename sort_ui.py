import gradio as gr

# Quick Sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Merge Sort algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

# Sorting function to be called by Gradio
def sort_array(array, algorithm):
    # Convert input string to a list of integers
    array = list(map(int, array.split(',')))
    # Select the appropriate sorting algorithm
    if algorithm == "Quick Sort":
        sorted_array = quick_sort(array)
    elif algorithm == "Merge Sort":
        sorted_array = merge_sort(array)
    return sorted_array

# Gradio interface
with gr.Blocks() as demo:
    # Add CSS for custom styling
    gr.HTML("""
    <style>
    body {background-color: #f0f8ff;}
    h1 {color: blue;}
    h3 {color: green;}
    .gr-button {color: white; background-color: blue;}
    </style>
    """)
    
    gr.Markdown("<h1>Array Sorting UI</h1>")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("<h3>Input Section</h3>")
            # Input field for array
            array_input = gr.Textbox(
                label="Enter array (comma-separated)",
                placeholder="e.g., 3,1,4,1,5,9,2,6,5"
            )
            # Radio buttons for algorithm selection
            algorithm_choice = gr.Radio(
                ["Quick Sort", "Merge Sort"],
                label="Select sorting algorithm"
            )
            # Button to trigger sorting
            sort_button = gr.Button("Sort Array")
        
        with gr.Column():
            gr.Markdown("<h3>Output Section</h3>")
            # Textbox to display sorted array
            result = gr.Textbox(label="Sorted Array")

    # Define what happens when the button is clicked
    sort_button.click(
        fn=sort_array,
        inputs=[array_input, algorithm_choice],
        outputs=result
    )

# Launch the Gradio demo with sharing enabled
demo.launch(share=True)
