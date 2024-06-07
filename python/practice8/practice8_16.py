# 方法1：import module_name
import example_module
example_module.example_function()

# 方法2：from module_name import function_name
from example_module import example_function
example_function()

# 方法3：from module_name import function_name as fn
from example_module import example_function as ef
ef()

# 方法4：import module_name as mn
import example_module as em
em.example_function()

# 方法5：from module_name import *
from example_module import *
example_function()

