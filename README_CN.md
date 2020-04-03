# Sublime Plan  [English](./README.md)  
> 这个插件每隔一段时间, 会遍历任务列表, 然后弹出提示框, 弹出的提示框一天之内不会弹出第二次  


## Task List  
```json  
{
    "tasks": {
        "welcome": {
            "overtime": "00:00:00",
            "message": "hello Sublime Text -- From sublime_plan",
        },
        "have_lunch": {
            "overtime": "12:00:00",
            "message": "have lunch everyday!",
        }
    }
}
```  

在 Sublime 的 User 目录中创建 `sublime-plan.sublime-settings`, 根据上面的格式编写任务列表.  


## Install
```
git clone https://github.com/floydawong/sublime_plan
git submodule init
```
