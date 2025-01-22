# README.md

## Project Overview
This project processes a WhatsApp chat record (`shiro.txt`) and uses it to train a character-level transformer-based language model to generate text. The workflow involves multiple stages, including preprocessing the chat data, cleaning it, and using it as input for the language model. The primary goal is to generate text based on patterns in the chat data.

## Files

### 1. **more.py**
This script processes the chat data to standardize and reformat the text.

#### Key Steps:
1. **Input:**
   - Reads the `input.txt` file generated in the preprocessing stage.
2. **Processing:**
   - Replaces the first occurrences of specific keywords (`Catoysigma` and `Ritesh`) with `User:` and `Output:`, respectively.
   - Processes each line iteratively.
3. **Output:**
   - Writes the updated lines back into `input.txt`.
4. **Note:**
   - Prints a confirmation message when the replacements are complete.

### 2. **text_proccess.py**
This script preprocesses the raw WhatsApp chat data (`shiro.txt`) to clean and extract relevant information.

#### Key Steps:
1. **Input:**
   - Reads `shiro.txt` containing the chat record.
2. **Cleaning:**
   - Removes unwanted characters using a predefined regex.
   - Skips lines with media or timestamps that do not contain text messages.
3. **Processing:**
   - Strips extra whitespace and extracts the message portion of each line.
4. **Output:**
   - Writes the processed messages to `input.txt`.
5. **Note:**
   - Ensures the output is clean and consistent for training the language model.

### 3. **main.py**
This script defines and trains a character-level language model using PyTorch.

#### Key Steps:
1. **Data Preparation:**
   - Reads `input.txt` as raw text.
   - Creates a vocabulary of unique characters.
   - Encodes the text into integer sequences.
   - Splits the data into training and validation sets.

2. **Model Architecture:**
   - Implements a transformer-based model with multiple attention heads and feedforward layers.
   - Includes positional and token embeddings.
   - Features:
     - Multi-Head Attention
     - Layer Normalization
     - Dropout for regularization

3. **Training:**
   - Uses the AdamW optimizer for parameter updates.
   - Evaluates loss periodically on both training and validation sets.
   - Generates sample text at the end of training.

4. **Text Generation:**
   - Generates new sequences based on the trained model by sampling one character at a time.

5. **Output:**
   - Prints generated text as a sequence of `User:` and `Output:` dialogues.

### Output Example
After training, the model generates text mimicking the structure and patterns observed in the input chat data. An example of the generated text is:

```
Output: I am not check
User: Sorry leave me
User: Kya
Output: Bhary karunga
Output: No
Output: ?
Output: Bola
Output: It's morning warro
...
```

## Requirements
- Python 3.8+
- PyTorch
- File `shiro.txt` containing WhatsApp chat records.

## Usage
1. Place the `shiro.txt` file in the same directory as the scripts.
2. Run `text_proccess.py` to preprocess the raw chat data:
   ```bash
   python text_proccess.py
   ```
3. Run `more.py` to reformat the processed data:
   ```bash
   python more.py
   ```
4. Train the language model using `main.py`:
   ```bash
   python main.py
   ```
5. Inspect the generated text from the model in the console output.

## Notes
- Ensure that the `shiro.txt` file contains properly formatted WhatsApp chat data.
- Adjust hyperparameters in `main.py` as needed for different datasets.
- The generated text quality depends on the size and diversity of the input data.


