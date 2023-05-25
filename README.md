
# design_pattern_python
设计模式-python， python design pattern,基于菜鸟教程的设计模式java实现进行了python重写 

[TOC]

## 写在前面

[菜鸟教程](https://www.runoob.com/design-pattern/design-pattern-tutorial.html) 中对常用的设计模式进行了汇总，实现上使用的是java。在本仓库里面对所有的教程涉及到的代码用python进行了重写，同样也有C++版本的实现在另一个仓库进行了管理
[C++ 设计模式](https://github.com/cf-zhang/design_patterns)

## [设计模式简介](https://www.runoob.com/design-pattern/design-pattern-intro.html)

![设计模式之间的关系](images/the-relationship-between-design-patterns.jpg)

## 创建型模式

这些设计模式提供了一种在创建对象的同时隐藏创建逻辑的方式，而不是使用 new 运算符直接实例化对象。这使得程序在判断针对某个给定实例需要创建哪些对象时更加灵活。	

### [工厂模式（Factory Pattern）](https://www.runoob.com/design-pattern/factory-pattern.html)

[factory_pattern.py](./factory_pattern.py)

![factory_pattern](./images/factory_pattern.jpg)

### [抽象工厂模式（Abstract Factory Pattern）](https://www.runoob.com/design-pattern/abstract-factory-pattern.html)

[abstract_factory_pattern.py](./abstract_factory_pattern.py)

![abstract_factory_pattern](./images/abstract_factory_pattern.jpg)

### [单例模式（Singleton Pattern）](https://www.runoob.com/design-pattern/singleton-pattern.html)

[singleton_pattern.py](./singleton_pattern.py)

![singleton_pattern](./images/singleton_pattern.jpg)


### [建造者模式（Builder Pattern）](https://www.runoob.com/design-pattern/builder-pattern.html)

[build_pattern.py](./builder_pattern.py)

![build_pattern](./images/build_pattern.svg)

### [原型模式（Prototype Pattern）](https://www.runoob.com/design-pattern/prototype-pattern.html)

[prototype_pattern.py](./prototype_pattern.py)

![prototype pattern](./images/prototype-pattern.png)

## 结构型模式

这些设计模式关注类和对象的组合。继承的概念被用来组合接口和定义组合对象获得新功能的方式。	

### [适配器模式（Adapter Pattern）](https://www.runoob.com/design-pattern/adapter-pattern.html)

[adapter_pattern.py](./adapter_pattern.py)

![adapter](./images/adaptor.png)

### [桥接模式（Bridge Pattern）](https://www.runoob.com/design-pattern/bridge-pattern.html)

[bridge_pattern.py](./bridge_pattern.py)

![bridge pattern](./images/bridge.svg)

### [过滤器模式（Filter、Criteria Pattern）](https://www.runoob.com/design-pattern/filter-pattern.html)

[filter_pattern.py](./filter_pattern.py)

![filter pattern](./images/20230510-filter.svg)

### [组合模式（Composite Pattern）](https://www.runoob.com/design-pattern/composite-pattern.html)

[composite_pattern.py](./composite_pattern.py)

![composite pattern](./images/20210817-composite-composite.svg)

### [装饰器模式（Decorator Pattern）](https://www.runoob.com/design-pattern/decorator-pattern.html)

[decorator_pattern.py](./decorator_pattern.py)

![decorator pattern](./images/20210420-decorator-1-decorator-decorator.svg)

### [外观模式（Facade Pattern）](https://www.runoob.com/design-pattern/facade-pattern.html)

[facade_pattern.py](./facade_pattern.py)

![facade pattern](./images/20201015-facade.svg)

### [享元模式（Flyweight Pattern）](https://www.runoob.com/design-pattern/flyweight-pattern.html)

[flyweight_pattern.py](./flyweight_pattern.py)

![flyweight pattern](./images/20201015-fiyweight.svg)

### [代理模式（Proxy Pattern）](https://www.runoob.com/design-pattern/proxy-pattern.html)

[proxy_pattern.py](./proxy_pattern.py)

![proxy pattern](./images/20211025-proxy.svg)

## 行为型模式
这些设计模式特别关注对象之间的通信。

### [责任链模式（Chain of Responsibility Pattern）]()

[chain_of_responsibility_pattern.py](./chain_of_responsibility_pattern.py)

### [命令模式（Command Pattern）]()

[command_pattern.py](./command_pattern.py)

### [解释器模式（Interpreter Pattern）]()

[interpreter_pattern.py](./interpreter_pattern.py)

### [迭代器模式（Iterator Pattern）]()

### [中介者模式（Mediator Pattern）]()

### [备忘录模式（Memento Pattern）]()

### [观察者模式（Observer Pattern）]()

### [状态模式（State Pattern）]()

### [空对象模式（Null Object Pattern）]()

### [策略模式（Strategy Pattern）]()

### [模板模式（Template Pattern）]()

### [访问者模式（Visitor Pattern）]()

## J2EE 模式

这些设计模式特别关注表示层。这些模式是由 Sun Java Center 鉴定的。	

## [MVC 模式（MVC Pattern）]()

## [业务代表模式（Business Delegate Pattern）]()

## [组合实体模式（Composite Entity Pattern）]()

## [数据访问对象模式（Data Access Object Pattern）]()

## [前端控制器模式（Front Controller Pattern）]()

## [拦截过滤器模式（Intercepting Filter Pattern）]()

## [服务定位器模式（Service Locator Pattern）]()

## [传输对象模式（Transfer Object Pattern）]()


