# PlaidCTF 2018 #

## Wait Wait ... Don't Shell Me! ##

### Challenge ###

[Challenge](https://ctftime.org/task/6070)

[Reference Write-Up](https://fortenf.org/e/ctfs/pwn/2018/05/07/plaidctf-2018-waitwait.html)

```
PCTF radio is hosting a new game show. Check it out at wwdsm.chal.pwning.xxx:6615.

Note: The server closes stdin/stdout before executing your shellcode.

> nc wwdsm.chal.pwning.xxx 6615
```



### Resources ###

#### Presentation ####

The presentation is provided in odp and pdf format.

#### Demonstration

The folder `demo` contains the sources and a Makefile that can be used to demonstrate both of the steps necessary for exploitation by example. Please note that this demonstration is crafted to run locally and does not behave exactly like the real challenge (binary was not provided).

##### Part 1 #####

If necessary, edit the offset of memory to read in`demo1.s:25`. Change into the `demo` folder, in one terminal run `make demo1_nc` and in another `make run_demo1`. The first terminal should show some output. Look for the offset of the string `"flag.txt"` which is necessary for Part 2. Note that this is a relative offset to whatever was encoded in `demo1.s:25`.

##### Part 2 #####

Edit `demo2.s:26` to use the offset obtained in Part 1 as path argument to the `open` syscall. Change into the `demo` folder, in one terminal run `make demo2_nc` and in another `make run_demo2`. The first terminal should show the (fake-)flag stored in `flag.txt`.

