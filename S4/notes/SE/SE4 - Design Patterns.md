---
tags: [SE]
title: SE4 - Design Patterns
created: '2020-05-21T18:07:23.750Z'
modified: '2020-05-23T08:29:48.405Z'
---

# SE4 - Design Patterns

<h3><font color="#BB86FC">Introduction</font></h3>

Be a good programmer and an efficient one, meaning take the chance to learn from others. 
Similar patterns occur over and over so do not reinvent the wheel and share knowledge of problem solving. Facilitate communication between programmers, and write elegant and graceful code. 

<h3><font color="#BB86FC">Design Patterns</font></h3>

A pattern is a description of the problem and the essence of its solution, it should be sufficiently abstract to be reused in different settings and often rely on object characteristics such as inheritance and polymorphism. 

A design pattern is a way of <font color="yellow">re-using abstract knowledge </font> about a (sw) design problem and its solution.


<h3><font color="#BB86FC">Pattern Elements</font></h3>

* Name
  * A meaningful pattern identifier
* Description
  * A description of the pattern
* Problem / Applicability description
* Solution Description
  * Not concrete design but template for design solution that can be instantiated in different ways.
* Consequences
  * The results and trade-offs of applying the pattern.

<h4><font color="#CF6679">Example :</font></h4>

* Name: Singleton
* Description: Ensure a class has only one instance and provide a global point of access to it.
* Problem/Applicability: used when only one object of a kind may exist in the system.
* Solution:
  * defines an instance operation that lets clients access its unique instance. 
  * Instance is a class operation
  * Responsible for creating and maintaining its own unique instance.


<h3><font color="#BB86FC">The Observer Pattern</font></h3>

The observer pattern is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

* Name: Observer
* Description:
  * Seperates the display of object state from the object itself.
* Problem/Applicability:
  * Used when multiple displays of state are needed.
* Solution:
  * See slide with UML description.
* Consequences:
  * Optimizations to enhance display performancec are impractical.

```mermaid
 classDiagram
      Observer <|-- ConcreteObserver
      Subject <|-- ConcreteSubject
      Observer o-- Subject
      Subject *-- Observer
      Observer : +Update()
      ConcreteObserver -- ConcreteSubject
      Subject : +Attach(Observer)
      Subject : +Detach(Observer)
      Subject : + Notify()
      class ConcreteObserver{
          +State observerState
          +Update()
      }
      class ConcreteSubject{
          +State subjectState
          +GetState()
      }
```


<h3><font color="#BB86FC">The Mediator Pattern</font></h3>

In software engineering, the mediator pattern defines an object that encapsulates how a set of objects interact. This pattern is considered to be a behavioral pattern due to the way it can alter the program's running behavior.

* Name: Mediator
* Description
  * Define an object that <font color="yellow">encapsulates</font> how a set of objects <font color="yellow">interact</font>. Mediator promotes <font color="yellow">loose coupling</font> by keeping objects from referring to each other explicitly.
* Problem/Applicability
  * Complex interaction exists.
* Consequences
  * Limits subclassing
  * Decouples colleagues
  * Simplifies object protocols
  * Abstracts how objects cooperate
  * Centralizes control

<h3><font color="#BB86FC">The Façade Pattern</font></h3>

The facade pattern (also spelled façade) is a software-design pattern commonly used in object-oriented programming. Analogous to a facade in architecture, a facade is an object that serves as a front-facing interface masking more complex underlying or structural code.

* Description: 
  * Provides a <font color="yellow"> unified interface to a set of interfaces in a subsytem </font> or defines a <font color="yellow">higher-level </font>interface that makes subsystem easier to use.
* Applicability
  * Need to provide a simple interface to a complex system.
  * Need to decouple a subsystem from its clients.
  * Need to provide an <font color="yellow">interface to a software layer</font>.
* Consequences
  * Shields clients from subsystem componenets
  * Promotes weak coupling between the subsystem and its clients.

```mermaid
graph TB
  subgraph subsystem classes
  c1[Class A] --> c2[Class B]
  c3[Class C] --> c1
  c4[Class D] --> c2
  end
  fac[Facade] --> c1
  fac --> c2
  fac --> c3
  fac --> c4
```

<h3><font color="#BB86FC">The Proxy Pattern</font></h3>

In computer programming, the proxy pattern is a software design pattern. A proxy, in its most general form, is a class functioning as an interface to something else. The proxy could interface to anything: a network connection, a large object in memory, a file, or some other resource that is expensive or impossible to duplicate. In short, a proxy is a wrapper or agent object that is being called by the client to access the real serving object behind the scenes.

* Description:
  * Provide a surrogate or placeholder for another object to control access to it.
* Problem/Applicability
  * Remote proxies can hide the fact that a real object is in <font color="yellow">another address space </font>.
  * Virtual proxies can <font color="yellow">create expensive objects </font>on demand.
  * Protection proxies can <font color="yellow">control access</font> to an object.
  * Smart references can perform <font color="yellow">additional action </font>above a simple pointer.

<h3><font color="#BB86FC">The Adapter Pattern</font></h3>

In software engineering, the adapter pattern is a software design pattern (also known as wrapper, an alternative naming shared with the decorator pattern) that allows the interface of an existing class to be used as another interface.[1] It is often used to make existing classes work with others without modifying their source code.

* Description:
  * Adapter lets classes work together that could not otherwise because of incompatible interfaces.
* Problem/Applicability
  * Need to use an existing class whose <font color="yellow">interface does not match </font>.
  * Need to make use of <font color="yellow">incompatible classes</font>.
* Consequences:
  * Class adapter commits to the concrete Adapter class.

<h3><font color="#BB86FC">The Composite Pattern</font></h3>

In software engineering, the composite pattern is a partitioning design pattern. The composite pattern describes a group of objects that are treated the same way as a single instance of the same type of object. The intent of a composite is to "compose" objects into tree structures to represent part-whole hierarchies.

* Definition:
  * Compose objects into tree structures to represent <font color="yellow">part-whole hierarchies </font>.
  * Composite lets clients <font color="yellow">treat individual objects and compositions of objects uniformly</font>.
* Problem/Applicability:
  * Any time there is <font color="yellow">partial overlap</font> in the capabilities of objects.

<h3><font color="#BB86FC">Types of Patterns</font></h3>

* Creational:
  * Singleton: A class of which only a single instance can exist.
* Structural Patterns:
  * Façade : A single class that represents an entire subsystem
  * Proxy : An object representing another object
  * Composite : A tree structure of simple and composite objects
  * Adapter : Match interfaces of different classes.
* Behavioral Patterns:
  * Mediator: Defines simplified communication between classes.
  * Observer: A way of notifying change to a number of classes.

<h3><font color="#BB86FC">Summary:</font></h3>

* Design patterns are generic, reusable design templates for OOP to be adapted by the programmer for faster and safer implementation.

* Three main types of patterns : <font color="red"> creational, structural and behavioral </font>.

