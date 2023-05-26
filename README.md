
# design_pattern_python
设计模式-python， python design pattern,基于菜鸟教程的设计模式java实现进行了python重写 

- [design\_pattern\_python](#design_pattern_python)
  - [写在前面](#写在前面)
  - [设计模式简介](#设计模式简介)
  - [创建型模式](#创建型模式)
    - [工厂模式（Factory Pattern）](#工厂模式factory-pattern)
    - [抽象工厂模式（Abstract Factory Pattern）](#抽象工厂模式abstract-factory-pattern)
    - [单例模式（Singleton Pattern）](#单例模式singleton-pattern)
    - [建造者模式（Builder Pattern）](#建造者模式builder-pattern)
    - [原型模式（Prototype Pattern）](#原型模式prototype-pattern)
  - [结构型模式](#结构型模式)
    - [适配器模式（Adapter Pattern）](#适配器模式adapter-pattern)
    - [桥接模式（Bridge Pattern）](#桥接模式bridge-pattern)
    - [过滤器模式（Filter、Criteria Pattern）](#过滤器模式filtercriteria-pattern)
    - [组合模式（Composite Pattern）](#组合模式composite-pattern)
    - [装饰器模式（Decorator Pattern）](#装饰器模式decorator-pattern)
    - [外观模式（Facade Pattern）](#外观模式facade-pattern)
    - [享元模式（Flyweight Pattern）](#享元模式flyweight-pattern)
    - [代理模式（Proxy Pattern）](#代理模式proxy-pattern)
  - [行为型模式](#行为型模式)
    - [责任链模式（Chain of Responsibility Pattern）](#责任链模式chain-of-responsibility-pattern)
    - [命令模式（Command Pattern）](#命令模式command-pattern)
    - [解释器模式（Interpreter Pattern）](#解释器模式interpreter-pattern)
    - [迭代器模式（Iterator Pattern）](#迭代器模式iterator-pattern)
    - [中介者模式（Mediator Pattern）](#中介者模式mediator-pattern)
    - [备忘录模式（Memento Pattern）](#备忘录模式memento-pattern)
    - [观察者模式（Observer Pattern）](#观察者模式observer-pattern)
    - [状态模式（State Pattern）](#状态模式state-pattern)
    - [空对象模式（Null Object Pattern）](#空对象模式null-object-pattern)
    - [策略模式（Strategy Pattern）](#策略模式strategy-pattern)
    - [模板模式（Template Pattern）](#模板模式template-pattern)
    - [访问者模式（Visitor Pattern）](#访问者模式visitor-pattern)
  - [J2EE 模式](#j2ee-模式)
    - [MVC 模式（MVC Pattern）](#mvc-模式mvc-pattern)
    - [业务代表模式（Business Delegate Pattern）](#业务代表模式business-delegate-pattern)
    - [组合实体模式（Composite Entity Pattern）](#组合实体模式composite-entity-pattern)
    - [数据访问对象模式（Data Access Object Pattern）](#数据访问对象模式data-access-object-pattern)
    - [前端控制器模式（Front Controller Pattern）](#前端控制器模式front-controller-pattern)
    - [拦截过滤器模式（Intercepting Filter Pattern）](#拦截过滤器模式intercepting-filter-pattern)
    - [服务定位器模式（Service Locator Pattern）](#服务定位器模式service-locator-pattern)
    - [传输对象模式（Transfer Object Pattern）](#传输对象模式transfer-object-pattern)


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

### [责任链模式（Chain of Responsibility Pattern）](https://www.runoob.com/design-pattern/chain-of-responsibility-pattern.html)

[chain_of_responsibility_pattern.py](./chain_of_responsibility_pattern.py)

![chain of responsibility pattern](./images/2021-chain-of-responsibility.svg)

### [命令模式（Command Pattern）](https://www.runoob.com/design-pattern/command-pattern.html)

[command_pattern.py](./command_pattern.py)

![command pattern](./images/20220427-command-1-command-1.svg)

### [解释器模式（Interpreter Pattern）](https://www.runoob.com/design-pattern/interpreter-pattern.html)

[interpreter_pattern.py](./interpreter_pattern.py)

![interpreter pattern](./images/interpreter_pattern_uml_diagram.jpg)

### [迭代器模式（Iterator Pattern）](https://www.runoob.com/design-pattern/iterator-pattern.html)

[iterator_patter.py](./iterator_pattern.py)

![iterator_pattern](./images/202107-23-iterator-pattern.png)

[iterator_pattern.py](./iterator_pattern.py)

### [中介者模式（Mediator Pattern）](https://www.runoob.com/design-pattern/mediator-pattern.html)

[mediator_pattern.py](mediator_pattern.py)

![mediator pattern](./images/mediator_pattern_uml_diagram.jpg)

### [备忘录模式（Memento Pattern）]()

[memento_pattern.py](./memento_pattern.py)

### [观察者模式（Observer Pattern）]()

[observer_pattern.py](observer_pattern.py)

### [状态模式（State Pattern）]()

[state_pattern.py](./state_pattern.py)

### [空对象模式（Null Object Pattern）]()

[null_object_pattern.py](null_object_pattern.py)

### [策略模式（Strategy Pattern）]()

[strategy_pattern.py](./strategy_pattern.py)

### [模板模式（Template Pattern）]()

[template_pattern.py](./template_pattern.py)

### [访问者模式（Visitor Pattern）]()

[visitor_pattern.py](./visitor_pattern.py)

## J2EE 模式

这些设计模式特别关注表示层。这些模式是由 Sun Java Center 鉴定的。	

### [MVC 模式（MVC Pattern）]()

[mvc_pattern.py](./mvc_pattern.py)

### [业务代表模式（Business Delegate Pattern）]()

[business_delegate_pattern.py](./business_delegate_pattern.py)

### [组合实体模式（Composite Entity Pattern）]()

[composite_entity_pattern.py](./composite_entity_pattern.py)

### [数据访问对象模式（Data Access Object Pattern）]()

[data_access_object_pattern.py](./data_access_object_pattern.py)

### [前端控制器模式（Front Controller Pattern）]()

[front_controller_pattern.py](./front_controller_pattern.py)

### [拦截过滤器模式（Intercepting Filter Pattern）]()

[intercepting_filter_pattern.py](./intercepting_filter_pattern.py)

### [服务定位器模式（Service Locator Pattern）]()

[service_locator_pattern.py](./service_locator_pattern.py)

### [传输对象模式（Transfer Object Pattern）]()

[transfer_object_pattern.py](./transfer_object_pattern.py)


