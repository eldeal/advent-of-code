package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/davecgh/go-spew/spew"
)

type Commands [][]string

func main() {
	in, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(in), "\n")

	var commands Commands
	for _, l := range lines {
		commands = append(commands, strings.Fields(string(l)))
	}

	system := map[string]int{}
	path := ""
	for i, cmd := range commands {
		if cmd[0] == "$" && cmd[1] == "cd" && cmd[2] != ".." {
			if cmd[2] == "/" {
				path = "/"
				continue
			}

			if path == "/" {
				path += cmd[2]
				continue
			}

			path += "/" + cmd[2]
			fmt.Println("The path is now " + path)
			continue
		}

		if cmd[0] == "$" && cmd[1] == "cd" && cmd[2] == ".." {
			parts := strings.Split(path, "/")
			path = strings.Join(parts[0:len(parts)-1], "/")
			fmt.Println("The path is now " + path)
			continue
		}

		if cmd[0] == "$" && cmd[1] == "ls" {
			fmt.Println("Scanning directory at " + path)
			d, n := commands.scanDir(path, i+1)
			i = n
			system[path] = d
		}
	}

	total := 0
	for k, v := range system {
		fmt.Println("Checking for subdirectories of " + k)
		fmt.Println("Current size is " + strconv.Itoa(v))
		for x, y := range system {
			if strings.Contains(x, k) && x != k {
				//fmt.Println("Found subdir: " + x + " is subdir of " + k)
				v += y
			}
		}
		fmt.Println("Directory: [" + k + "] Size: [" + strconv.Itoa(v) + "]")

		if v <= 100000 {
			total += v
			fmt.Println("Added to total")
			continue
		}

		fmt.Println("NOT included in total")
	}

	spew.Dump(total)

}

func (c Commands) scanDir(path string, i int) (int, int) {
	d := 0
	var n int
	for n = i; c[n][0] != "$" && n < len(c)-1; n++ {
		if c[n][0] != "dir" {
			fmt.Println("Adding size of  " + c[n][0])
			size, err := strconv.Atoi(c[n][0])
			if err != nil {
				panic(err)
			}
			d += size
		}
	}
	fmt.Println("Returning the size of all files and new index")
	spew.Dump(d)
	spew.Dump(n)
	return d, n
}
