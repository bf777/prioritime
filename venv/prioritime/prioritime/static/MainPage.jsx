import React from 'react';
import ReactDOM from 'react-dom';
import CourseForm from '../components/CourseForm.js';

require('../static/MainPage.scss')

export default class MainPage extends React.Component {
  render() {
    return (
    <div>
          <div className="pimg1">
              <div className="logo">
                  <br/><br/><br/><br/><br/><br/>
                  <img src="http://imageshack.com/a/img923/7441/G7WdO3.gif"/>
                  <div className="underText">Optimize your learning schedule</div>
              </div>
          </div>

                  <div>
                    <section className="section section-light">
                        <div>
                        <h2>Project Description</h2>
                        <p>Prioritime is a web-based platform that enables users to intuitively organize their tasks that need to be completed for the day, based on the ability to import their google calendar data as well as integrating with their university learning platform,
                            to be able to help individuals make better use of their time and make smarter decisions that is tailored to their current academic process in school.
                        </p>
                        </div>
                    </section>
                  </div>

                  <div className="pimg2">
                      <div className="ptext">
                          <span className="border">
                                  Be consistent</span>

                          <span className="border">
                                   Be persistent</span>

                          <span className="border">
                                   Be outstanding</span>
                      </div>
                  </div>
                  <section className="section section-dark">
                  <div>

                      <h2>Designed For Students</h2>
                      <p> We realized that one of the biggest headaches for students is figuring out what their priorities should be - whether it be working on a group project, or which course to study for first. Poor time management and planning results in bad grades,
                          which is very discouraging and frustrating. With Prioritime, the system would be able to suggest activities based on machine learning algorithms on what to do first, based on the course number, the year of study, length of each className, and
                          the frequency. The integration with google calendars will also extract personal tasks and appointments, and will suggest to the user what to focus on first on that specific day.
                          <br/> <br/>
                      </p>
                      </div>
                  </section>

                  <div className="margin"> </div>
                  <section className="section section-dark">
                  <div>

                      <h2> Why Prioritime? </h2>
                      <p>
                      <i>“It does not do well to leave a live dragon out of your calculations, if you live near one”
                                  <br/>                                                                          – The Hobbit</i>

                      </p>
                      <p> Exams, Assignments, Personal commitments. With a forward thinking mindset, PrioriTime will help you tackle each task efficiently and effectively. Optimize your schedule to let you relax and focus on the tasks themselves. Whether it be figuring
                          out time for assignments, tests, out of className activities, or friends, PrioriTime will help you figure out the best routine for you, according to your needs. Don’t just do them in time, crush them. </p>

                  </div>
                  </section>

                  <div className="pimg3">
                      <div className="ptext">
                          <span className="border">Relax</span>

                          <span className="border">Breathe</span>
                          <span className="border">Prioritize</span>
                      </div>
                  </div>

                  <section className="section-dark" id="boxes">
                      <div className="container">
                          <h1>
                            Pain Points
                          </h1>
                          <hr/> <br/> <br/><br/>
                          <div className="box">
                              <img src="http://imageshack.com/a/img922/3307/yTqLJH.png"/>
                              <h3>Lack of Transparency</h3>
                              <p>Instructors sometimes do not give a full overview of how students are progressing in their courses, and grade transparency is something that is lacking for many school systems. Students are not able to know their grades til the end of
                                  the term
                              </p>
                          </div>
                          <div className="box">
                              <img src="http://imageshack.com/a/img924/9003/bZKbRa.png"/>
                              <h3>Progress Tracking</h3>
                              <p>
                                  When working on a project, students lack the tools to be able to track their progress when working with a team, as many tasks are dispersed across different people. Prioritime allows individual tracking so that students can focus on what they can complete,
                                  on time.
                              </p>
                          </div>
                          <div className="box">
                              <img src="http://imageshack.com/a/img922/2629/8sn4mX.png"/>
                              <h3>Uncertainty</h3>
                              <p>School isn’t everything, which is why Prioritime integrates with google calendar to extract non-school tasks and data as well. Prioritime will be able to give reminders on upcoming appointments and whether they will collide with project
                                  due dates, and give suggestions on which projects to complete first to give users room to breathe</p>
                          </div>
                      </div>
                  </section>


                  <div className="margin"> </div>





                  <div className="margin"> </div>


                  <section className="section section-light">
                      <div className="pimg4">
                          <div className="container">

                                  <h2>Just Type In Your Courses</h2>
                                  <h3>And we will do the rest</h3>

                          </div>




                      </div>

                  </section>




                  <div className="margin"></div>





                  <section className="section-light" id="faces">
                      <div className="container">

                              <h1> Meet the Geeks</h1>


                          <hr/>
                          <div className="face">
                              <img src="http://imageshack.com/a/img924/5355/eJarKa.png"/>
                              <h3>Brandon</h3>
                          </div>
                          <div className="face">
                              <img src="http://imageshack.com/a/img923/269/CaOFij.png"/>
                              <h3>Shamit</h3>
                          </div>
                          <div className="face">
                              <img src="http://imageshack.com/a/img922/6143/ohbJal.png"/>
                              <h3>Zarrin</h3>
                          </div>
                          <div className="face">
                              <img src="http://imageshack.com/a/img922/3351/pEQh0E.png"/>
                              <h3>Pablo</h3>
                          </div>
                          <div className="face">
                              <img src="http://imageshack.com/a/img923/2495/MpPKUw.png"/>
                              <h3>Dani</h3>
                          </div>

                      </div>
                  </section>


                  <footer>
                      <p>EduHacks 2017, Project Prioritime &copy; 2017</p>
                      <div className="small-text">
                          Stock images courtesy of<a href="https://www.pexels.com/"> pexels.com</a><br/> Parallax CSS theme inspired from <a href="http://www.traversymedia.com/"> Traversy Media</a> <br/> LightBox inspired from <a href="https://www.w3schools.com/">w3schools.com</a>
                      </div>
                  </footer>
          </div>
      );
}
}
