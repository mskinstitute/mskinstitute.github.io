
fetch('assets/js/courses.json')
  .then(res => res.json())
  .then(data => {
    
    const keys = Object.keys(data);

    keys.forEach(key => {
      const course_name = data[key]['name'];
      const course_image = data[key]['featured_image'];
      const course_video = data[key]['featured_video'];
      const course_description = data[key]['description'];
      const course_parent_course = data[key]['parent_course'];
      const course_skill_level = data[key]['skill_level'];
      const course_language = data[key]['language'];
      const course_duration = data[key]['duration'];
      const course_enrolled = data[key]['enrolled'];
      const course_discount = data[key]['discount'];
      const course_fee = data[key]['fee'];
      const course_certificate = data[key]['certificate'];
      const course_public_status = data[key]['public_status'];
      const course_lectures = data[key]['lectures'];
      const course_link = data[key]['link'];
      const course_curiculam = data[key]['curiculam'];

      const courses_El = document.querySelector('#courses');
      
      const course_item = `
                    <div class="card border rounded-xl shadow p-2 lift sk-fade">
                        <div class="card-zoom position-relative">
                            <a href="${course_link}" class="card-img sk-thumbnail d-block">
                                <img class="rounded shadow-light-lg" src="${course_image}" alt="${course_name}">
                            </a>

                            <span
                                class="badge sk-fade-bottom badge-lg badge-purple badge-pill badge-float bottom-0 left-0 mb-4 ms-4">
                                <span class="text-white text-uppercase fw-bold font-size-xs">${course_skill_level}</span>
                            </span>
                        </div>

                        <div class="card-footer px-2 pb-2 mb-1 pt-4 position-relative">

                            <a href="${course_link}"><span class="mb-1 d-inline-block text-gray-800">${course_parent_course}</span></a>

                            <div class="position-relative">
                                <a href="${course_link}" class="d-block stretched-link">
                                    <h4 class="line-clamp-2 h-md-48 h-lg-58 me-md-6 me-lg-10 me-xl-4">${course_name}</h4>
                                </a>

                                <div class="d-lg-flex align-items-end flex-wrap mb-1">
                                    <div class="star-rating mb-1 mb-lg-0 me-lg-3">
                                        <div class="rating" style="width:50%;"></div>
                                    </div>

                                    <div class="font-size-sm mx-2">
                                        <span>5.45 (5.8k+ reviews)</span>
                                    </div>
                                </div>

                                <div class="row mx-n2 align-items-end">
                                    <div class="col px-2">
                                        <ul class="nav mx-n3">
                                            <li class="nav-item px-3">
                                                <div class="d-flex align-items-center">
                                                    <div class="me-2 d-flex icon-uxs text-secondary">
                                                        <!-- Icon -->
                                                        <svg width="20" height="20" viewBox="0 0 20 20" fill="none"
                                                            xmlns="http://www.w3.org/2000/svg">
                                                            <path
                                                                d="M17.1947 7.06802L14.6315 7.9985C14.2476 7.31186 13.712 6.71921 13.0544 6.25992C12.8525 6.11877 12.6421 5.99365 12.4252 5.88303C13.0586 5.25955 13.452 4.39255 13.452 3.43521C13.452 1.54098 11.9124 -1.90735e-06 10.0197 -1.90735e-06C8.12714 -1.90735e-06 6.58738 1.54098 6.58738 3.43521C6.58738 4.39255 6.98075 5.25955 7.61414 5.88303C7.39731 5.99365 7.1869 6.11877 6.98502 6.25992C6.32752 6.71921 5.79178 7.31186 5.40787 7.9985L2.8447 7.06802C2.33612 6.88339 1.79688 7.26044 1.79688 7.80243V16.5178C1.79688 16.8465 2.00256 17.14 2.31155 17.2522L9.75312 19.9536C9.93073 20.018 10.1227 20.0128 10.2863 19.9536L17.7278 17.2522C18.0368 17.14 18.2425 16.8465 18.2425 16.5178V7.80243C18.2425 7.26135 17.704 6.88309 17.1947 7.06802ZM10.0197 1.5625C11.0507 1.5625 11.8895 2.40265 11.8895 3.43521C11.8895 4.46777 11.0507 5.30792 10.0197 5.30792C8.98866 5.30792 8.14988 4.46777 8.14988 3.43521C8.14988 2.40265 8.98866 1.5625 10.0197 1.5625ZM9.23844 18.1044L3.35938 15.9703V8.91724L9.23844 11.0513V18.1044ZM10.0197 9.67255L6.90644 8.54248C7.58164 7.51892 8.75184 6.87042 10.0197 6.87042C11.2875 6.87042 12.4577 7.51892 13.1329 8.54248L10.0197 9.67255ZM16.68 15.9703L10.8009 18.1044V11.0513L16.68 8.91724V15.9703Z"
                                                                fill="currentColor"></path>
                                                        </svg>

                                                    </div>
                                                    <div class="font-size-sm">${course_lectures} Chapters</div>
                                                </div>
                                            </li>
                                            <li class="nav-item px-3">
                                                <div class="d-flex align-items-center">
                                                    <div class="me-2 d-flex icon-uxs text-secondary">
                                                        <!-- Icon -->
                                                        <svg width="16" height="16" viewBox="0 0 16 16"
                                                            xmlns="http://www.w3.org/2000/svg">
                                                            <path
                                                                d="M14.3164 4.20996C13.985 4.37028 13.8464 4.76904 14.0067 5.10026C14.4447 6.00505 14.6667 6.98031 14.6667 8C14.6667 11.6759 11.6759 14.6667 8 14.6667C4.32406 14.6667 1.33333 11.6759 1.33333 8C1.33333 4.32406 4.32406 1.33333 8 1.33333C9.52328 1.33333 10.9543 1.83073 12.1387 2.77165C12.4259 3.00098 12.846 2.95296 13.0754 2.66471C13.3047 2.37663 13.2567 1.95703 12.9683 1.72803C11.5661 0.613607 9.8016 0 8 0C3.58903 0 0 3.58903 0 8C0 12.411 3.58903 16 8 16C12.411 16 16 12.411 16 8C16 6.77767 15.7331 5.60628 15.2067 4.51969C15.0467 4.18766 14.6466 4.04932 14.3164 4.20996Z"
                                                                fill="currentColor"></path>
                                                            <path
                                                                d="M7.99967 2.66663C7.63167 2.66663 7.33301 2.96529 7.33301 3.33329V7.99996C7.33301 8.36796 7.63167 8.66663 7.99967 8.66663H11.333C11.701 8.66663 11.9997 8.36796 11.9997 7.99996C11.9997 7.63196 11.701 7.33329 11.333 7.33329H8.66634V3.33329C8.66634 2.96529 8.36768 2.66663 7.99967 2.66663Z"
                                                                fill="currentColor"></path>
                                                        </svg>

                                                    </div>
                                                    <div class="font-size-sm">${course_duration} Month</div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div class="col-auto px-1 text-right">
                                        <ins class="btn btn-primary px-2 py-1">View More</ins>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
      `
      
      const course_El = document.createElement('div');
      course_El.classList.add('col-md');
      course_El.classList.add('pb-4');
      course_El.classList.add('pb-md-7');
      course_El.innerHTML = course_item;
      courses_El.appendChild(course_El);

    });

  });