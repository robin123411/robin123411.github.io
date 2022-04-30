# robin123411.github.io
test website

## Welcome to My Channel.

I will share what I have learned about Java.  

### HIT JAVA

JavaEE 是 Java Web 开发当中事实上的标准，诸多框架也都是建立在 JavaEE 的 API 基础之上的。为了从头理解 Java Web 开发，我们将从一个最简单的 JavaEE Servlet 应用开始，一步一步进入 Java Web 开发的世界。

### 准备工作
要完成这个教程，你只需要有网络就可以了，首先下载 IntelliJ IDEA Community 版。没错，我们就是故意要使用 Community 版，尽管 Utimate 版对 JavaEE 开发的支持更好，但是更好的工具却可能让我们忽略底层的细节。Community 版对于入门来说已经足够。

然后你需要下载 JavaSE 的 JDK，也就是大家使用最多的 JDK 版本。示例使用的 1.8.0 版本。

最后你需要一个 Servlet Container，去 Tomcat 网站下载一个版本，主要要和 JDK 的版本要求相匹配。示例使用的是 Tomcat 8.5.0。

### 第一个 Servlet
首先创建一个工程，选择好 JDK 版本，一路 Next 就可以了。创建好工程之后，我们创建一个新的 Servlet。首先在左边的 src 上右键创建一个 package，然后在 package 上右键，创建一个 

    Java Class：

    package com.skyline;

    import javax.servlet.*;
    import java.io.IOException;
    import java.io.PrintWriter;

        public class MyFirstServlet implements Servlet {
            public void init(ServletConfig config) throws ServletException {
                System.out.println("Init");
            }

        public void service(ServletRequest request, ServletResponse response)
                throws ServletException, IOException {
            System.out.println("From service");
            PrintWriter out = response.getWriter();
            out.println("Hello, Java Web.");
        }

        public void destroy() {
            System.out.println("Destroy");
        }

        public String getServletInfo() {
            return null;
        }

        public ServletConfig getServletConfig() {
            return null;
        }
    }
这时候代码上会报很多错误，核心原因是 javax.servlet 这个包找不到。前面提的过 Servlet API 是包含在 JavaEE 当中的。为了方便，我们直接使用 Tomcat 附带的 servlet-api.jar 包。

在 IDEA 中打开 Library Settings（External Libraries 下面的任意一项右键 -> Open Library Settings.

T Unit2 next...


四渡赤水

