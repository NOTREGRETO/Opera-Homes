import os
import re

files = [
    'blogs/index.html',
    'blogs/jayanagar-premium-flats.html',
    'blogs/flat-buyer-checklist-bangalore.html',
    'blogs/jp-nagar-vs-jayanagar-investment.html'
]

new_footer = """    <!-- Footer Start -->
    <footer class="main-footer">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-6">
                    <div class="about-footer">
                        <div class="footer-logo">
                            <img src="../assets/images/logos/logo-footer.png" alt="Opera Homes">
                        </div>
                        <div class="about-footer-content">
                            <p>Opera Homes with over 15 years of Experience in shaping the emerging urban landscape., has elevated itself of creating some of the landmark residential and commercial projects in bangalore.</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6">
                    <div class="footer-links">
                        <h3>Follow Links</h3>
                        <ul>
                            <li><a href="../pages/about.html">About Us</a></li>
                            <li><a href="../pages/residential.html">Residential</a></li>
                            <li><a href="../pages/commercial.html">Commercial</a></li>
                            <li><a href="../pages/projects.html">Gallery</a></li>
                            <li><a href="index.html">Blogs</a></li>
                            <li><a href="../pages/contact.html">Contact Us</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6">
                    <div class="footer-links">
                        <h3>Social Links</h3>
                        <div class="footer-social-links">
                            <ul>
                                <li><a href="#"><i class="fa-brands fa-facebook-f"></i></a></li>
                                <li><a href="#"><i class="fa-brands fa-instagram"></i></a></li>
                                <li><a href="#"><i class="fa-brands fa-youtube"></i></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="footer-contact-box footer-links">
                        <h3>Contact Details</h3>
                        <div class="footer-contact-item">
                            <div class="icon-box"><i class="fa-solid fa-phone" style="color:#64748b;"></i></div>
                            <div class="footer-contact-content"><p>+91 8041230476</p></div>
                        </div>
                        <div class="footer-contact-item">
                            <div class="icon-box"><i class="fa-solid fa-phone" style="color:#64748b;"></i></div>
                            <div class="footer-contact-content"><p>+91 9740213520</p></div>
                        </div>
                        <div class="footer-contact-item">
                            <div class="icon-box"><i class="fa-solid fa-envelope" style="color:#64748b;"></i></div>
                            <div class="footer-contact-content"><p>info.sales@operahomes.in</p></div>
                        </div>
                        <div class="footer-contact-item">
                            <div class="icon-box"><i class="fa-solid fa-location-dot" style="color:#64748b;"></i></div>
                            <div class="footer-contact-content"><p>No. 149 - 3rd Floor - Above KFC Restaurant Jayanagar 4th Block, Bangalore - 560011</p></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-copyright">
                <div class="row align-items-center">
                    <div class="col-lg-12">
                        <div class="footer-copyright-text">
                            <p>Copyright &copy; 2024 All Rights Reserved.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <!-- Footer End -->"""

for f in files:
    path = os.path.join('c:\\Users\\parth\\Downloads\\hnm\\Opera-Homes', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Use regex to find and replace the footer section
        pattern = re.compile(r'<!-- Footer Start -->.*?<!-- Footer End -->', re.DOTALL)
        if pattern.search(content):
            content = pattern.sub(new_footer, content)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Successfully updated {f}')
        else:
            print(f'Footer markers not found in {f}')
    else:
        print(f'File not found: {f}')
