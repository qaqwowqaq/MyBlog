// src/types/shims-css.d.ts

declare module "*.css" {
    const classes: { [key: string]: string };
    export default classes;
  }
  
  declare module "*.scss" {
    const classes: { [key: string]: string };
    export default classes;
  }
  
  // 如果你使用的是其他CSS预处理器，如 Less，可以添加类似的声明
  declare module "*.less" {
    const classes: { [key: string]: string };
    export default classes;
  }

  