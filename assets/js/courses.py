import json

course_list = {

    '0001': {
        'name': 'MS-Word: Beginner',
        'featured_image': 'assets/img/products/word.png',
        'featured_video': 'youtube_video_link_word',
        'description': '''Unlock the full potential of MS-Word with MSK Institute's comprehensive course, designed for beginners and those looking to improve their skills. From creating professional documents to using advanced formatting and editing features, you will become proficient in handling word processing tasks efficiently.

        By the end of the course, you will be able to create reports, letters, resumes, and other documents that are polished, well-structured, and professional. Gain insights into features such as mail merge, templates, styles, and collaboration tools.''',
        'parent_course': 'MS Office Suite',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1 Month',
        'deadline': '3 Months',
        'enrolled': 3,
        'discount': 20,
        'fee': 999,
        'certificate': True,
        'public_status': True,
        'lectures': 12,
        'link': 'assets/templates/word.html',
        'curiculam': {
            '01 Introduction': [
                '1.1 What is MS-Word?',
                '1.2 Overview of the Word Interface'
            ],
            '02 Document Creation': [
                '2.1 Creating and Saving Documents',
                '2.2 Formatting Text and Paragraphs'
            ],
            '03 Tables and Graphics': [
                '3.1 Inserting Tables',
                '3.2 Adding and Formatting Images'
            ],
            '04 Styles and Templates': [
                '4.1 Using and Modifying Styles',
                '4.2 Working with Templates'
            ],
            '05 Advanced Features': [
                '5.1 Mail Merge',
                '5.2 Track Changes and Comments'
            ],
            '06 Projects': [
                '6.1 Creating a Formal Report',
                '6.2 Resume Building Project'
            ]
        }
    },
    '0002': {
        'name': 'MS-PowerPoint: Beginner',
        'featured_image': 'assets/img/products/powerpoint.png',
        'featured_video': 'youtube_video_link_powerpoint',
        'description': '''Learn how to create dynamic presentations with MS-PowerPoint at MSK Institute. This course takes you through the basics of presentation design, including slide layout, transitions, animations, and integrating multimedia elements. By the end, you will be capable of delivering impactful presentations that captivate audiences.

        You will also explore advanced features like using master slides, customizing themes, and collaborating on presentations to take your skills to the next level.''',
        'parent_course': 'MS Office Suite',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1 Month',
        'deadline': '3 Months',
        'enrolled': 2,
        'discount': 20,
        'fee': 999,
        'certificate': True,
        'public_status': True,
        'lectures': 10,
        'link': 'assets/templates/powerpoint.html',
        'curiculam': {
            '01 Introduction': [
                '1.1 What is MS-PowerPoint?',
                '1.2 Overview of the PowerPoint Interface'
            ],
            '02 Slide Creation': [
                '2.1 Creating and Organizing Slides',
                '2.2 Applying Themes and Layouts'
            ],
            '03 Visual Elements': [
                '3.1 Inserting Images and Videos',
                '3.2 Working with Charts and SmartArt'
            ],
            '04 Transitions and Animations': [
                '4.1 Adding Transitions between Slides',
                '4.2 Animating Slide Content'
            ],
            '05 Advanced Features': [
                '5.1 Master Slides and Custom Themes',
                '5.2 Collaborating on Presentations'
            ],
            '06 Projects': [
                '6.1 Creating a Business Presentation',
                '6.2 Educational Presentation Project'
            ]
        }
    },
    '0003': {
        'name': 'MS-Excel: Beginner',
        'featured_image': 'assets/img/products/excel.png',
        'featured_video': 'youtube_video_link_excel',
        'description': '''Master the powerful spreadsheet software MS-Excel with MSK Institute's course designed to help you understand data management, calculations, and analysis. Starting from the basics of spreadsheet navigation to more advanced topics like pivot tables, charts, and functions, you will become proficient in data handling and reporting.

        This course emphasizes practical applications, ensuring you can use Excel to solve real-world problems, from personal finance to business analysis.''',
        'parent_course': 'MS Office Suite',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1.5 Months',
        'deadline': '3.5 Months',
        'enrolled': 4,
        'discount': 20,
        'fee': 999,
        'certificate': True,
        'public_status': True,
        'lectures': 15,
        'link': 'assets/templates/excel.html',
        'curiculam': {
            '01 Introduction': [
                '1.1 What is MS-Excel?',
                '1.2 Spreadsheet Basics'
            ],
            '02 Data Entry and Formatting': [
                '2.1 Entering and Editing Data',
                '2.2 Formatting Cells and Worksheets'
            ],
            '03 Formulas and Functions': [
                '3.1 Basic Formulas',
                '3.2 Common Functions (SUM, IF, VLOOKUP)'
            ],
            '04 Data Visualization': [
                '4.1 Creating Charts',
                '4.2 Formatting and Customizing Charts'
            ],
            '05 Data Analysis': [
                '5.1 Pivot Tables',
                '5.2 Data Sorting and Filtering'
            ],
            '06 Projects': [
                '6.1 Financial Spreadsheet Project',
                '6.2 Data Analysis Project'
            ]
        }
    },
    '0004': {
        'name': 'HTML: Beginner',
        'featured_image': 'assets/img/products/html.png',
        'featured_video': 'youtube_video_link_html',
        'description': '''Welcome to MSK Institute's HTML course. This course is designed for those who are stepping into the world of web development. At MSK Institute, we provide high-quality training to ensure you understand how HTML structures websites and applications. Starting with the basics, you will learn to create structured, accessible web pages, advancing to more complex topics like forms, multimedia embedding, and SEO best practices.
        
        You will gain hands-on experience, building fully functional websites, ensuring your skills are aligned with industry standards. From writing your first HTML tag to mastering semantic HTML, this course will make you a confident web developer.''',
        'parent_course': 'Web Designing',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1 Month',
        'deadline': '3 Months',
        'enrolled': 15,
        'discount': 12,
        'fee': 1699,
        'certificate': True,
        'public_status': True,
        'lectures': 15,
        'link': 'assets/templates/html.html',
        'curiculam': {
            '01 Introduction': [
                '1.1 Introduction to HTML',
                '1.2 Setting up Development Environment'
            ],
            '02 Basic Tags': [
                '2.1 Understanding HTML Tags',
                '2.2 Paragraphs, Headings, and Links'
            ],
            '03 Lists': [
                '3.1 Ordered Lists',
                '3.2 Unordered Lists',
                '3.3 Nested Lists'
            ],
            '04 Images': [
                '4.1 Adding Images',
                '4.2 Image Attributes and Best Practices'
            ],
            '05 Tables': [
                '5.1 Creating Tables',
                '5.2 Table Formatting and Design'
            ],
            '06 Forms': [
                '6.1 Creating Forms',
                '6.2 Form Input Types and Validation'
            ],
            '07 Semantic HTML': [
                '7.1 Importance of Semantic HTML',
                '7.2 Using Semantic Elements Correctly'
            ],
            '08 Multimedia': [
                '8.1 Embedding Audio and Video',
                '8.2 IFrames and Interactive Content'
            ],
            '09 SEO': [
                '9.1 Introduction to SEO',
                '9.2 Optimizing HTML for Search Engines'
            ],
            '10 Projects': [
                '10.1 Basic Webpage Project',
                '10.2 Intermediate Webpage Project'
            ]
        }
    },
    '0005': {
        'name': 'CSS: Beginner',
        'featured_image': 'assets/img/products/css.png',
        'featured_video': 'youtube_video_link_css',
        'description': '''MSK Institute's CSS course is designed to teach you how to style and layout web pages with precision. Through hands-on exercises and projects, you will master the art of responsive design, typography, color schemes, animations, and modern CSS techniques. Whether you're a beginner or have some experience, this course will elevate your web design skills.

        By the end of the course, you will be able to create visually appealing, user-friendly websites that adapt to different screen sizes and devices. The course also focuses on industry best practices and tools for modern web development.''',
        'parent_course': 'Web Designing',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1.5 Months',
        'deadline': '3.5 Months',
        'enrolled': 15,
        'discount': 12,
        'fee': 1699,
        'certificate': True,
        'public_status': True,
        'lectures': 18,
        'link': 'assets/templates/css.html',
        'curiculam': {
            '01 Introduction to CSS': [
                '1.1 What is CSS?',
                '1.2 How CSS Works with HTML'
            ],
            '02 CSS Selectors': [
                '2.1 Basic Selectors',
                '2.2 Advanced Selectors',
                '2.3 Pseudo-classes and Pseudo-elements'
            ],
            '03 Styling Text': [
                '3.1 Font Properties',
                '3.2 Text Alignment and Spacing'
            ],
            '04 Colors and Backgrounds': [
                '4.1 Working with Colors',
                '4.2 Adding Backgrounds'
            ],
            '05 Box Model': [
                '5.1 Understanding the Box Model',
                '5.2 Margin, Padding, and Border'
            ],
            '06 Layouts': [
                '6.1 Flexbox',
                '6.2 CSS Grid',
                '6.3 Positioning Elements'
            ],
            '07 Responsive Design': [
                '7.1 Media Queries',
                '7.2 Responsive Layout Techniques'
            ],
            '08 CSS Animation': [
                '8.1 Keyframes and Transitions',
                '8.2 Creating Interactive Animations'
            ],
            '09 Projects': [
                '9.1 Styling a Simple Web Page',
                '9.2 Responsive Web Design Project'
            ]
        }
    },
    '0006': {
        'name': 'Bootstrap 5: Beginner',
        'featured_image': 'assets/img/products/bootstrap.png',
        'featured_video': 'youtube_video_link_bootstrap',
        'description': '''Join MSK Institute's Bootstrap 5 course and enhance your front-end development skills by learning one of the most popular frameworks for creating responsive websites. This course covers everything from the fundamentals of Bootstrap to advanced topics like custom components, layout systems, and utility classes.

        By the end of the course, you will be able to quickly design and build responsive websites with modern layouts and components that are optimized for both desktop and mobile devices.''',
        'parent_course': 'Web Development',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1.5 Months',
        'deadline': '4 Months',
        'enrolled': 15,
        'discount': 12,
        'fee': 1699,
        'certificate': True,
        'public_status': True,
        'lectures': 18,
        'link': 'assets/templates/bootstrap.html',
        'curiculam': {
            '01 Introduction to Bootstrap 5': [
                '1.1 What is Bootstrap 5?',
                '1.2 Setting Up Bootstrap in Projects'
            ],
            '02 Layout and Grid System': [
                '2.1 Understanding the Grid System',
                '2.2 Building Responsive Layouts'
            ],
            '03 Components': [
                '3.1 Navigation and Navbar',
                '3.2 Forms, Buttons, and Cards'
            ],
            '04 Customizing Bootstrap': [
                '4.1 Using Bootstrap Utilities',
                '4.2 Customizing Themes and Styles'
            ],
            '05 Advanced Features': [
                '5.1 JavaScript Components in Bootstrap',
                '5.2 Customizing Bootstrap with SASS'
            ],
            '06 Projects': [
                '6.1 Basic Bootstrap Project',
                '6.2 Advanced Bootstrap Project'
            ]
        }
    },
    '0007': {
        'name': 'JavaScript: Beginner',
        'featured_image': 'assets/img/products/javascript.png',
        'featured_video': 'youtube_video_link_javascript',
        'description': '''Master JavaScript with MSK Institute's comprehensive course designed to transform beginners into proficient developers. As a powerful tool for creating interactive and dynamic web content, JavaScript is essential for any web developer. Our course provides in-depth coverage of JavaScript basics and more advanced topics like DOM manipulation, event handling, and working with APIs.
        
        You will also learn essential programming concepts like functions, loops, and objects, all while building hands-on projects. With MSK Institute's guidance, you'll be equipped to tackle real-world web development challenges.''',
        'parent_course': 'Web Development',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '2 Months',
        'deadline': '4 Months',
        'enrolled': 15,
        'discount': 12,
        'fee': 1699,
        'certificate': True,
        'public_status': True,
        'lectures': 25,
        'link': 'assets/templates/javascript.html',
        'curiculam': {
            '01 Introduction to JavaScript': [
                '1.1 JavaScript Overview',
                '1.2 Setting up the Environment'
            ],
            '02 Variables and Data Types': [
                '2.1 Variables in JavaScript',
                '2.2 Data Types and Type Coercion'
            ],
            '03 Operators and Expressions': [
                '3.1 Arithmetic and Logical Operators',
                '3.2 Control Flow with Conditionals'
            ],
            '04 Functions': [
                '4.1 Defining and Calling Functions',
                '4.2 Function Parameters and Return Values'
            ],
            '05 Loops and Iteration': [
                '5.1 For and While Loops',
                '5.2 Iterating Arrays and Objects'
            ],
            '06 Objects and Arrays': [
                '6.1 Understanding Objects',
                '6.2 Working with Arrays'
            ],
            '07 DOM Manipulation': [
                '7.1 Selecting and Manipulating DOM Elements',
                '7.2 Event Handling'
            ],
            '08 APIs and AJAX': [
                '8.1 What is an API?',
                '8.2 Fetching Data using AJAX and Fetch API'
            ],
            '09 ES6 Features': [
                '9.1 Let and Const',
                '9.2 Arrow Functions',
                '9.3 Template Literals'
            ],
            '10 Projects': [
                '10.1 Basic JavaScript App',
                '10.2 Intermediate JavaScript Project'
            ]
        }
    },
    '0008': {
        'name'          : 'Python Basic: Beginner',
        'featured_image': 'assets/img/products/python.png',
        'featured_video': 'youtube_video_link',
        'description'   : '''Welcome to MSK Institute's Python Basic course, designed specifically for aspiring programmers seeking a structured path to mastering Python. As a premier coding institute, MSK Institute is committed to providing high-quality education that prepares students for the demands of the modern tech landscape. This course takes you from the fundamentals to an intermediate level, ensuring you gain a solid understanding of Python and its versatile applications.
        
        Whether you're new to programming or looking to build your skills, this course covers all the essential topics to help you grow as a confident Python developer. Starting with an easy-to-follow setup guide, we ensure you can install Python and configure the right tools to run your code smoothly. From there, you'll be introduced to Python's intuitive syntax and the basics of programming, such as variables, data types, and operators.
        
        At MSK Institute, we believe in hands-on learning. That's why this course includes numerous exercises to give you practical experience working with Python. You'll dive into core programming structures like loops, conditional statements, and functions, which form the backbone of any Python application. You'll also work with data structures like lists, tuples, sets, and dictionaries, ensuring you're ready to handle data effectively.
        
        As you progress, our curriculum covers more advanced topics, such as Object-Oriented Programming (OOP). You will learn about classes, inheritance, and polymorphism, which are crucial for writing efficient, reusable, and scalable code. Additionally, we focus on real-world tasks, such as file handling, where you will learn to read from and write to files, work with different formats, and manage data securely.
        
        By the end of the course, you will have the confidence to build Python applications independently, reinforced by projects that allow you to apply your skills in a practical context. At MSK Institute, we don't just offer knowledge; we offer career-building skills that align with industry demands. Upon completion, you will receive an official MSK Institute certification, demonstrating your proficiency and commitment to learning.
        ''',
        'parent_course' : "Python Development",
        'skill_level'    : "Beginner to Intermediate",
        'language'      : "Hindi/English",
        'duration'      : "1 Month",
        'deadline'      : "3 Months",
        'enrolled'      : 22,
        'discount'      : 60,
        'fee'           : 2499,
        'certificate'   : True,
        'public_status' : True,
        'lectures'      : 21,
        'link'          : 'assets/templates/python.html',
        'curiculam'     : {
            '01 Introduction': [ 
                '1.1 Course Introduction', 
                '1.2 Python Introduction' 
            ],
            '02 Setup': [ 
                '2.1 Installing Python', 
                '2.2 Setting up IDE', 
                '2.3 Running Your First Program' 
            ],
            '03 Syntax': [
                '3.1 Basic Syntax', 
                '3.2 Code Indentation', 
                '3.3 Writing Python Code'
            ],
            '04 Comments': [
                '4.1 Single-Line Comments', 
                '4.2 Multi-Line Comments', 
                '4.3 Commenting Best Practices'
            ],
            '05 Variables': [
                '5.1 Defining Variables', 
                '5.2 Variable Naming Rules', 
                '5.3 Variable Scope'
            ],
            '06 Data Types': [
                '6.1 Basic Data Types', 
                '6.2 Type Checking', 
                '6.3 Type Conversion'
            ],
            '07 Numbers': [
                '7.1 Integer and Float', 
                '7.2 Complex Numbers', 
                '7.3 Mathematical Operations'
            ],
            '08 Casting': [
                '8.1 Implicit Casting', 
                '8.2 Explicit Casting', 
                '8.3 Casting Best Practices'
            ],
            '09 Operators': [
                '9.1 Arithmetic Operators', 
                '9.2 Comparison Operators', 
                '9.3 Logical Operators', 
                '9.4 Assignment Operators'
            ],
            '10 Strings': [
                '10.1 Creating Strings', 
                '10.2 String Methods', 
                '10.3 String Slicing'
            ],
            '11 List': [
                '11.1 Creating Lists', 
                '11.2 List Methods', 
                '11.3 List Comprehension'
            ],
            '12 Tuple': [
                '12.1 Creating Tuples', 
                '12.2 Accessing Tuple Elements', 
                '12.3 Tuple Operations'
            ],
            '13 Sets': [
                '13.1 Creating Sets', 
                '13.2 Set Methods', 
                '13.3 Set Operations'
            ],
            '14 Dictionaries': [
                '14.1 Creating Dictionaries', 
                '14.2 Accessing Dictionary Elements', 
                '14.3 Dictionary Methods'
            ],
            '15 Conditional Statements': [
                '15.1 If-Else Statements', 
                '15.2 Nested Conditions', 
                '15.3 Conditional Expressions'
            ],
            '16 Loops': [
                '16.1 For Loops', 
                '16.2 While Loops', 
                '16.3 Loop Control Statements'
            ],
            '17 Functions': [
                '17.1 Defining Functions', 
                '17.2 Function Arguments', 
                '17.3 Return Statements', 
                '17.4 Lambda Functions'
            ],
            '18 OOP (Object-Oriented Programming)': [
                '18.1 Classes and Objects', 
                '18.2 Inheritance', 
                '18.3 Polymorphism', 
                '18.4 Encapsulation', 
                '18.5 Abstraction'
            ],
            '19 File Handling': [
                '19.1 Opening Files', 
                '19.2 Reading and Writing Files', 
                '19.3 File Methods', 
                '19.4 Handling File Exceptions'
            ],
            '20 Modules': [
                '21.1 Importing Modules', 
                '21.2 Built-in Modules', 
                '21.3 Creating Your Own Modules'
            ],
            '21 Projects': [
                '22.1 Beginner Project Ideas', 
                '22.2 Intermediate Project Ideas', 
                '22.3 Project Development Best Practices'
            ]
        }
    },
    '0009': {
        'name': 'SQL: Beginner',
        'featured_image': 'assets/img/products/sql.png',
        'featured_video': 'youtube_video_link_sql',
        'description': '''MSK Institute's SQL course is designed to teach you how to manage databases effectively. You will learn the fundamentals of database management, SQL syntax, and how to write queries for real-world applications. This course covers everything from basic data retrieval to complex joins, subqueries, and performance optimization.

        By the end of the course, you will be able to create, manage, and query databases to handle large-scale data sets, preparing you for roles in data analysis and backend development.''',
        'parent_course': 'Database Management',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1 Month',
        'deadline': '3 Months',
        'enrolled': 25,
        'discount': 10,
        'fee': 1999,
        'certificate': True,
        'public_status': True,
        'lectures': 20,
        'link': 'assets/templates/sql.html',
        'curiculam': {
            '01 Introduction to SQL': [
                '1.1 What is SQL?',
                '1.2 Setting Up a Database Environment'
            ],
            '02 Basic Queries': [
                '2.1 SELECT Statements',
                '2.2 Filtering Data with WHERE'
            ],
            '03 Data Manipulation': [
                '3.1 Inserting, Updating, and Deleting Data',
                '3.2 Using Aggregate Functions'
            ],
            '04 Joins': [
                '4.1 Inner Joins',
                '4.2 Outer Joins',
                '4.3 Self Joins'
            ],
            '05 Subqueries': [
                '5.1 Writing Subqueries',
                '5.2 Advanced Subquery Techniques'
            ],
            '06 Performance Optimization': [
                '6.1 Indexing and Query Optimization',
                '6.2 Database Normalization'
            ],
            '07 Projects': [
                '7.1 Basic SQL Project',
                '7.2 Advanced SQL Project'
            ]
        }
    },
    '0010': {
        'name': 'NumPy: Beginner',
        'featured_image': 'assets/img/products/numpy.png',
        'featured_video': 'youtube_video_link_numpy',
        'description': '''MSK Institute's NumPy course is designed for individuals looking to gain proficiency in numerical computing using Python. This course covers the essential aspects of the NumPy library, which is fundamental for data science, machine learning, and scientific computing.

        From creating and manipulating arrays to performing advanced mathematical operations, you will learn to leverage NumPy’s capabilities for real-world data processing. By the end of the course, you will be well-equipped to use NumPy in conjunction with other Python libraries for data analysis and machine learning.''',
        'parent_course': 'Python Development',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '2 Weeks',
        'deadline': '2 Months',
        'enrolled': 18,
        'discount': 15,
        'fee': 1499,
        'certificate': True,
        'public_status': True,
        'lectures': 15,
        'link': 'assets/templates/numpy.html',
        'curiculam': {
            '01 Introduction to NumPy': [
                '1.1 What is NumPy?',
                '1.2 Installing and Setting Up NumPy'
            ],
            '02 Arrays': [
                '2.1 Creating Arrays',
                '2.2 Indexing and Slicing Arrays',
                '2.3 Array Manipulation'
            ],
            '03 Mathematical Operations': [
                '3.1 Basic Arithmetic with NumPy Arrays',
                '3.2 Aggregate Functions',
                '3.3 Element-Wise Operations'
            ],
            '04 Advanced Operations': [
                '4.1 Broadcasting',
                '4.2 Linear Algebra',
                '4.3 Random Numbers and Distributions'
            ],
            '05 Projects': [
                '5.1 NumPy for Data Analysis Project',
                '5.2 NumPy for Machine Learning Project'
            ]
        }
    },
    '0011': {
        'name': 'Power BI: Beginner',
        'featured_image': 'assets/img/products/powerbi.png',
        'featured_video': 'youtube_video_link_powerbi',
        'description': '''MSK Institute's Power BI course teaches you how to create interactive visualizations and business intelligence reports. This course covers data import, modeling, and visualization, enabling you to transform raw data into insightful dashboards and reports.

        You will learn to connect to various data sources, create customized visuals, and share your reports with others. By the end of this course, you will be able to use Power BI to analyze and visualize data for business decision-making.''',
        'parent_course': 'Data Analysis',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1 Month',
        'deadline': '3 Months',
        'enrolled': 17,
        'discount': 15,
        'fee': 1499,
        'certificate': True,
        'public_status': True,
        'lectures': 18,
        'link': 'assets/templates/powerbi.html',
        'curiculam': {
            '01 Introduction to Power BI': [
                '1.1 What is Power BI?',
                '1.2 Power BI Interface Overview'
            ],
            '02 Connecting to Data': [
                '2.1 Importing Data',
                '2.2 Connecting to Multiple Data Sources'
            ],
            '03 Data Modeling': [
                '3.1 Creating Relationships Between Tables',
                '3.2 Data Cleaning and Transformation'
            ],
            '04 Data Visualization': [
                '4.1 Creating Charts and Graphs',
                '4.2 Customizing Visuals'
            ],
            '05 Sharing Reports': [
                '5.1 Publishing Reports to Power BI Service',
                '5.2 Collaborating on Power BI Reports'
            ],
            '06 Projects': [
                '6.1 Building a Business Intelligence Dashboard',
                '6.2 Advanced Data Analysis Project'
            ]
        }
    },
    '0012': {
        'name': 'Photoshop: Beginner',
        'featured_image': 'assets/img/products/photoshop.png',
        'featured_video': 'youtube_video_link_photoshop',
        'description': '''MSK Institute's Photoshop course is designed for individuals looking to enhance their graphic design skills. This course will take you through the basics of image editing, manipulation, and graphic creation. You'll explore Photoshop's wide range of tools, including layers, filters, and effects.

        By the end of this course, you will be proficient in creating professional-grade designs, enhancing photos, and preparing digital assets for various media platforms. Whether you're a beginner or looking to refine your design skills, this course will give you the hands-on experience needed to succeed.''',
        'parent_course': 'Graphic Design',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1.5 Months',
        'deadline': '3 Months',
        'enrolled': 17,
        'discount': 15,
        'fee': 1999,
        'certificate': True,
        'public_status': True,
        'lectures': 25,
        'link': 'assets/templates/coming_soon.html',
        'curiculam': {
            '01 Introduction to Photoshop': [
                '1.1 Interface Overview',
                '1.2 Setting Up Your Workspace'
            ],
            '02 Basic Tools': [
                '2.1 Selection Tools',
                '2.2 Move Tool',
                '2.3 Transform Tools'
            ],
            '03 Layers': [
                '3.1 Understanding Layers',
                '3.2 Working with Layer Masks',
                '3.3 Layer Blending Modes'
            ],
            '04 Image Editing': [
                '4.1 Adjusting Colors and Exposure',
                '4.2 Retouching Techniques',
                '4.3 Removing Backgrounds'
            ],
            '05 Text and Shapes': [
                '5.1 Adding and Customizing Text',
                '5.2 Creating and Manipulating Shapes'
            ],
            '06 Effects and Filters': [
                '6.1 Applying Filters',
                '6.2 Using Smart Objects',
                '6.3 Special Effects'
            ],
            '07 Projects': [
                '7.1 Basic Design Project',
                '7.2 Intermediate Design Project'
            ]
        }
    },
    '0013': {
        'name': 'Illustrator: Beginner',
        'featured_image': 'assets/img/products/illustrator.png',
        'featured_video': 'youtube_video_link_illustrator',
        'description': '''MSK Institute's Illustrator course equips you with the skills to create stunning vector graphics for both print and digital media. Learn to use Illustrator's powerful tools to design logos, icons, and illustrations with precision.

        This course covers everything from basic shape creation to more advanced techniques like working with typography and gradients. By the end of this course, you'll be able to produce high-quality vector artwork for professional use.''',
        'parent_course': 'Graphic Design',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1 Month',
        'deadline': '3 Months',
        'enrolled': 17,
        'discount': 15,
        'fee': 1999,
        'certificate': True,
        'public_status': True,
        'lectures': 22,
        'link': 'assets/templates/coming_soon.html',
        'curiculam': {
            '01 Introduction to Illustrator': [
                '1.1 What is Adobe Illustrator?',
                '1.2 Setting Up Your Workspace'
            ],
            '02 Basic Tools': [
                '2.1 Selection Tools',
                '2.2 Pen Tool Basics',
                '2.3 Shape Tools'
            ],
            '03 Working with Paths': [
                '3.1 Drawing and Modifying Paths',
                '3.2 Creating Custom Shapes'
            ],
            '04 Typography': [
                '4.1 Working with Type',
                '4.2 Customizing Fonts and Styles'
            ],
            '05 Color and Gradients': [
                '5.1 Applying Colors and Gradients',
                '5.2 Working with Swatches'
            ],
            '06 Exporting and Printing': [
                '6.1 Preparing Files for Print',
                '6.2 Exporting for Web'
            ],
            '07 Projects': [
                '7.1 Logo Design Project',
                '7.2 Illustration Project'
            ]
        }
    },
    '0014': {
        'name': 'CorelDRAW: Beginner',
        'featured_image': 'assets/img/products/coreldraw.png',
        'featured_video': 'youtube_video_link_coreldraw',
        'description': '''MSK Institute's CorelDRAW course is designed for those looking to master vector graphic design. You will learn to use CorelDRAW’s tools to create illustrations, logos, brochures, and more.

        By the end of this course, you will be proficient in creating professional-quality vector graphics and layouts for print and web media. This course offers a complete guide from the basics to more advanced techniques.''',
        'parent_course': 'Graphic Design',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1.5 Months',
        'deadline': '3 Months',
        'enrolled': 17,
        'discount': 15,
        'fee': 1999,
        'certificate': True,
        'public_status': True,
        'lectures': 24,
        'link': 'assets/templates/coming_soon.html',
        'curiculam': {
            '01 Introduction to CorelDRAW': [
                '1.1 Overview of CorelDRAW Interface',
                '1.2 Customizing Workspace'
            ],
            '02 Drawing Tools': [
                '2.1 Pen Tool',
                '2.2 Freehand Drawing',
                '2.3 Shape Tools'
            ],
            '03 Working with Text': [
                '3.1 Adding Text',
                '3.2 Text Formatting'
            ],
            '04 Colors and Fills': [
                '4.1 Applying Colors and Fills',
                '4.2 Working with Gradients'
            ],
            '05 Layers and Effects': [
                '5.1 Using Layers',
                '5.2 Applying Effects'
            ],
            '06 Exporting and Printing': [
                '6.1 Exporting for Web and Print',
                '6.2 Printing Preparation'
            ],
            '07 Projects': [
                '7.1 Logo Design',
                '7.2 Brochure Design'
            ]
        }
    },
    '0015': {
        'name': 'Tally: Beginner',
        'featured_image': 'assets/img/products/tally.png',
        'featured_video': 'youtube_video_link_tally',
        'description': '''MSK Institute's Tally course offers a comprehensive guide to accounting and financial management using Tally software. This course is designed to help you manage business accounts, inventory, and taxes effectively.

        By the end of this course, you will have a strong foundation in using Tally for business and financial management, including GST compliance, voucher entry, and generating financial reports.''',
        'parent_course': 'Accounting',
        'skill_level': 'Beginner to Intermediate',
        'language': 'Hindi/English',
        'duration': '1 Month',
        'deadline': '3 Months',
        'enrolled': 18,
        'discount': 25,
        'fee': 3999,
        'certificate': True,
        'public_status': True,
        'lectures': 20,
        'link': 'assets/templates/coming_soon.html',
        'curiculam': {
            '01 Introduction to Tally': [
                '1.1 Overview of Tally ERP',
                '1.2 Setting Up a Company in Tally'
            ],
            '02 Accounting in Tally': [
                '2.1 Ledger Creation',
                '2.2 Voucher Entry',
                '2.3 Financial Statements'
            ],
            '03 Inventory Management': [
                '3.1 Managing Stock Items',
                '3.2 Stock Groups and Categories'
            ],
            '04 GST in Tally': [
                '4.1 Configuring GST',
                '4.2 GST Return Filing'
            ],
            '05 Reporting in Tally': [
                '5.1 Profit & Loss Statement',
                '5.2 Balance Sheet and Cash Flow Statements'
            ],
            '06 Projects': [
                '6.1 Accounting and Inventory Project',
                '6.2 GST Filing Project'
            ]
        }
    },

}


# print( course_list['0002'][ 'curiculam' ][ '02 Basic Tags' ][1]  )

f = open('assets/js/courses.json', 'w')
f.write(json.dumps(course_list, indent=4))