---
title: SE5 - Defensive Programming
created: '2020-05-21T15:35:52.695Z'
modified: '2020-05-23T08:29:11.865Z'
---

# SE5 - Defensive Programming

## Defensive Programming

* Prevention is better than cure; therefore, we use defensive programming. It ensures the continuing function of a piece of software in spit of unforseable usage of said software.

* Good design yields better product
  * Defending against errors avoids lengthy debugging sessions.

* Good design should be evident in code
  * Code is executable; comments aren't.
  * Key design checkpoints should be checked by your code.


<h3><font color="#BB86FC">Invariants</font></h3>

Invariants are conditions that do not vary, they are used as mileposts in your code.

* <font color="yellow">Loop invariants:</font> True at beginning of each loop iteration and after termination if all went well.
* <font color="yellow">Class invariants:</font> True before and after each method call.
  * All constructors should place their object in a valid state.
  * All methods should leave their object in a valid state.
    * pre-condition and post conditionn together should guarantee this
    * better than blind coding and testing
* <font color="yellow">Method invariants:</font>
  * Pre and post conditions
  * Part of "Design-by-contract" meaning that users must meet preconditions of the method and so the developer guarantees post-conditions.

<h3><font color="#BB86FC">Enforcing Invariants</font></h3>

* <font color="yellow">Assertions:</font> force-terminate program
  * For programmer errors that don't depend on end user, non-public member functions.
* <font color="yellow">Exceptions:</font> break flow of control
  * For pre-conditions on public member functions.
* <font color="yellow">Return codes:</font> data-oriented, keep flow of control
  * Post-conditions are usually a method's output.

<h4><font color="#CF6679">Assertions</font></h4>

* `assert()` macro $\rightarrow$ around since C.
* If argument is false:
  * prints expression, file and line number
  * then calls `abort`.
* Can be turned off using `NDEBUG`.

<h4><font color="#CF6679">Exceptions</font></h4>

* Interrupt flow of control and ripple up calling hierarchy
  * Until matching try/catch embrace 
  * Otherwise abort program
* Exceptions are classes
  * `throw()` instantiates exception object.
  * can have parameters  
  * catch sensitive per exception type
* Can have multiple `catch()`
  * `catch()` sensitive to any excception type.

<h4><font color="#CF6679">Return Codes</font></h4>

* Methods have a return parameter
  * If method has a regular result then we can reserve otherwise unused value
    * i.e `NULL` for string, `-1`for int, ...
* Single-return functions : use a local result variable.

<h3><font color="#BB86FC">Structured Programming</font></h3>

* Structured Programming is a componenet level-design technique which uses only small set of programming constructs.

* Principle: building blocks to enter at top & leave at bottom
  * <b>Good :</b> sequence ";"condition, repitition
  * <b>Bad :</b>(computed) goto; break; continue; ...
* Advantage: less complex code $\rightarrow$ easier to read + test + maintain
  * Measurable quality: small complexity (e.g., cyclometric)

<h4><font color="#CF6679">Loops:</font></h4>

* Use simple loop, nested loops and concatenated loops.
* Banning GOTO. 

<h3><font color="#BB86FC">Code Guides:</font></h3>

* A code guide is a set of rules to which programmers must adhere within a company or project.
* Twofold purpose 
  * Have uniform style 
    * less surprises, better learning curve for newbies.
    * codify best practice, what is acknowledged to be advantageous.

<h3><font color="#BB86FC">Core Coding Rules</font></h3>

* Reflect before typing
  * why are you doing what you are doing?
* Be pedantic
  * As far as ever possible, make it foolproof.
  * No monkey trick.
* Design cost-aware
  * Is it worth the effort?
  * Is it maintainable?
