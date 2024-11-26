# About

This repository was adapted from https://github.com/florianbuetow/solve-it-with-code-advent-2023/tree/main which was graciously shared with our cohort.

We are in the first iteration of [Jeremy Howard's](https://jeremy.fast.ai) new course [Solve It With Code](https://solveit.fast.ai), by [fast.ai](https://www.fast.ai)

This repository contains my solutions to the Advent of Code 2023 challenges, crafted using the engineering process taught in the course.

## Table of Challenges

| Day | Challenge                       | Solution Code | Time Complexity | Space Complexity | Challenge Link |
|-----|---------------------------------|---------------|-----------------|------------------|----------------|
| 1   | Trebuchet?!                     | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/1) |
| 2   | Cube Conundrum                  | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/2) |
| 3   | Gear Ratios                     | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/3) |
| 4   | Scratchcards                    | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/4) |
| 5   | If You Give A Seed A Fertilizer | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/5) |
| 6   | Wait For It                     | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/6) |
| 7   | Camel Cards                     | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/7) |
| 8   | Haunted Wasteland               | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/8) |
| 9   | Mirage Maintenance              | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/9) |
| 10  | Pipe Maze                       | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/10) |
| 11  | Cosmic Expansion                | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/11) |
| 12  | Hot Springs                     | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/12) |
| 13  | Point of Incidence              | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/13) |
| 14  | Parabolic Reflector Dish        | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/14) |
| 15  | Lens Library                    | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/15) |
| 16  | The Floor Will Be Lava          | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/16) |
| 17  | Clumsy Crucible                 | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/17) |
| 18  | Lavaduct Lagoon                 | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/18) |
| 19  | Aplenty                         | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/19) |
| 20  | Pulse Propagation               | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/20) |
| 21  | Step Counter                    | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/21) |
| 22  | Sand Slabs                      | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/22) |
| 23  | A Long Walk                     | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/23) |
| 24  | Never Tell Me The Odds          | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/24) |
| 25  | Snowverload                     | Unsolved      |                 | -                | -              | [adventofcode.com](https://adventofcode.com/2023/day/25) |

## Repository Structure

```bash
.
├── .env                            # Environment variables file (contains AOC_SESSION)
├── challenges.json                 # JSON file containing challenge titles and numbers
├── Dockerfile                      # Defines the Docker image for running the tools
├── README.md                       # Generated README file
├── README.template                 # Template for generating README.md
├── data/                           # Directory containing puzzle input files
├── docker_entrypoint.sh            # Script that handles different operations inside Docker container
├── generate_file_templates.py      # Script to generate solution file templates
├── generate_readme.py              # Script to generate README.md from template
├── puzzle_scraper.py               # Script to download puzzle inputs from AoC website
├── requirements.txt                # Python package dependencies
├── run_aoc_tools.sh                # Shell script to run Docker operations
└── solutions/                      # Directory containing solution files
```


## Repository Tools

This repository includes several Docker-based tools to help manage Advent of Code solutions. All tools are containerized, requiring only Docker installation (no local Python installation needed).

Recommended first-time setup order:
1. Run scrape to get puzzle inputs
2. Run templates to create solution files
3. Run readme to generate initial README

The available tools are:

1. **Puzzle Input Scraper**

    __Note:__ The input data for each challenge differs by user. If you are using this project as a template for your own solutions, you will need to obtain your own input data:

    1. Log in to the [Advent of Code](https://adventofcode.com)
    2. Open browser Developer Tools (F12)
    3. Go to Application/Storage > Cookies
    4. Copy the value of the 'session' cookie
    5. Create a `.env` file:
    ```bash
        touch .env
    ```
    6. Add your session cookie to `.env`:
        ```
        AOC_SESSION=your_session_cookie_value
        ```

   Downloads puzzle inputs from Advent of Code website and writes them to the `data/` directory:
   ```bash
   ./run_aoc_tools.sh scrape
   ```


2. **Solution Templates Generator**
   Creates template files for all puzzle solutions and writes them to the `solutions/` directory:
   ```bash
   ./run_aoc_tools.sh templates
   ```

3. **README Generator**
   Updates this README with current solution status:
   ```bash
   ./run_aoc_tools.sh readme
   ```



Generating the `README.md` file updates the cells of the challenges table based on the metadata from the `challenges.json` file the content (!) of the solution files automatically.

__Note:__ The time and space complexity are extracted from the solution files by looking for lines that start with `Time complexity:` and `Space complexity:` respectively. Please ensure that these lines are present in your solution files as well. Here are some valid examples:
```python
"""
...
Time complexity: O(...)
Space complexity: O(...)
...
"""
```
or
```python
...
# Time complexity: O(...)
...
# Space complexity: O(...)
...
```

*Before you can use the repository tools, follow these steps:*

#### 0. Prerequisites

- Clone this repository.
- Ensure that Docker is installed and running on your system.

#### 1. Make the Bash Script Executable

Run the following command to make the script executable:

```bash
chmod +x ./run_aoc_tools.sh
```

#### 2. Build and Run the Docker Container

Run either of the following commands based on your needs:
```bash
./run_aoc_tools.sh scrape
```
or
```bash
   ./run_aoc_tools.sh templates
   ```
or
```bash
./run_aoc_tools.sh readme
```

- This will build the Docker image each time it is run to avoid file caching issues.
- It will then run the Docker container to execute one of the scripts that generates the data in your local directory.