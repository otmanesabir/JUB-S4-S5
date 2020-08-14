---
deleted: true
favorited: true
title: SE3 - UML
created: '2020-05-21T15:35:40.204Z'
modified: '2020-05-22T10:23:51.332Z'
---

# SE3 - UML

## UML

<h3><font color="#BB86FC">What is UML?</font></h3>

UML (<font color="yellow">Unified Modeling Language</font>) is the standard language for specifying, visualizing, constructing and documenting all the artifacts of a software system. There a couple main digram types :

* Use Case Diagram (functional)
* Activity / Action Diagram (behavioral)
* Class Diagram (structural)
* State Diagram (behavioral)
* Sequence Diagram (behavioral)
* ... (many more)

<h3><font color="#BB86FC">Use Case Diagrams</font></h3>

The use case digrams allows us to visualize relationships between actors and use cases. it also allows to capture high level alternate scenarios, the main elements are :

* Use case, which is a chunk of functionality and <b>not</b> a software module.
* Actor, someone or something interacting with system under development.


<h3><font color="#BB86FC">Activity Diagram</font></h3>

This diagram represents the overall ***flow of control*** and shows a graphical workflow of user -perceived activities and actions. 


<h3><font color="#BB86FC">Class Diagrams</font></h3>

Class is a collection of objects witha common structure, behavior, relatioships and semantics. 
It can be displayed as a box with up to 3 componenets (Name, List of attributes, and list of operations). <br>
Class modeling elements include :
* Classes with structure + behavior
* Relationships
* Multiplicity and navigation indicators
* Role names

<h4><font color="#CF6679">Class Diagrams : Relationships</font></h4>

Class Diagram Relationships are used to model that two objects can talk or communicate by :
* <font color="yellow">Association - </font> bi-directional connection between classes.
  * a broad term that encompasses just about any logical connection or relationship between classes. For example, passenger and airline may be linked.
* <font color="yellow">Aggregation - </font> stronger form: "has a"
  * For example, the class “library” is made up of one or more books, among other materials. In aggregation, the contained classes are not strongly dependent on the lifecycle of the container. In the same example, books will remain so even when the library is dissolved.
* <font color="yellow">Dependency - </font> weaker form
  * For example, a shoulder bag’s side pocket will also cease to exist once the shoulder bag is destroyed.

<h4><font color="#CF6679">Class Diagrams : Multiplicities, Navigation</font></h4>

<font color="yellow">Multiplicity numbers & intervals </font> denote number of instances that can/must participate in relationship instance
  * 0...1 | may have one
  * 1 | must have one
  * 0.. | may have many
  * 1..* | has at least one

<font color="">Arrow head</font> to denote, traversable only in this direction.


<h4><font color="#CF6679">Class Diagrams : Inheritance</font></h4>

<font color="yellow">Inheritance </font> is the relation between subclass and superclass ("is a"). Subclass instances have all properties specified in superclass, plus the specific ones defined with the subclass. 

<h3><font color="#BB86FC">Sequence Diagrams</font></h3>

Sequecne diagrams display <font color="yellow"> object interactions </font> arranged in a <font color="yellow"> time sequence </font>. They're usually good for showing what's going on and driving requirements when interacting with customers. 

* How many SDs? 
  * for every basic flow of every use case.
  * for high-level, risky scenarios.

<h3><font color="#BB86FC">Sequence vs Activity Diagrams</font></h3>

<table>
<th>
  <td>Diagram </td>
  <td>Level of Detail</td>
  <td>Emhpasis</td>
</th>
<tr>
  <td>Activity diagram</td>
  <td>User-perceived actions</td>
  <td>Internal state transitions</td>
</tr>
<tr>
  <td>Sequence Diagram</td>
  <td>Actors + system componenets</td>
  <td>Componenet interaction</td>
</tr>
</table>

<h3><font color="#BB86FC">State Transition Diagrams</font></h3>

These diagrams show life history of a given class and is typically used for ones that have a lot of dynamic behavior. This also be defined using the sequence diagrams by picking classes which are on a lot of sequence diagrams (getting and sending a lot of messages).


<h3><font color="#BB86FC">UML Summary</font></h3>

* UML knows several diagram types to capture different aspects of a software system
  * Structural, functional and behavioral.
* Mutual interrelations
  * use them to do consistency & plausability cross checking.

<h3><font color="#BB86FC">UML 2.0</font></h3>

Substantially revised from UML 1.0, in particular for <b><font color="yellow">Model-Driven Architechture</font></b>
* <font color="yellow">Infrastracture:</font> core of architechture, profiles, stereotypes.
* <font color="yellow">Superstructure:</font> static & dynamic model elements.
* <font color="yellow">Object Constraint Language:</font> formalize assertions and rules.
* <font color="yellow">Diagram Interchange:</font> UML exchange format.

It's main goals are to speed up the process, give higher quality, more reusability and increase long-term usability.


## Summary

* UML is an industry standard for visually describing all aspects during software life cycle. It allows us to do so given the variety of different diagrams we can make (Use case diagram, Activity Diagram, Sequence Diagram, Class Diagram, State diagram, ...).

* A good approach is that if more work done in the beginning (before coding starts) then :
1. better design (less flaws and more consistency)
2. Fewer costly surprises late at integration
3. Better planning
4. Higher customer satisfaction, better career.

