import { setActiveLink, handleSidebar } from "./utils.min.js";

document.addEventListener("DOMContentLoaded", () => {
  setActiveLink();
  handleSidebar();

  const emailJsPublicKey = "o25JYcOD9t6qyLJvg";
  const emailJsServiceID = "service_8ve3b9t";
  const emailJsTemplateId = "template_joq4eek";

  emailjs.init({ publicKey: emailJsPublicKey });

  document.querySelector("#contact-form-submit").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.querySelector("#contact-form-name");
    const email = document.querySelector("#contact-form-email");
    const subject = document.querySelector("#contact-form-subject");
    const description = document.querySelector("#contact-form-description");
    const privacyPolicy = document.querySelector("#contact-form-privacy-policy");

    if (privacyPolicy.checked) {
      const formData = new FormData();
      formData.append("name", name.value),
        formData.append("email", email.value),
        formData.append("subject", subject.value),
        formData.append("description", description.value);

      try {
        const response = await emailjs.send(
          emailJsServiceID,
          emailJsTemplateId,
          Object.fromEntries(formData),
        );
        if (response.status === 200) {
          alert("Your email has been sent, we will get back to shortly");

          // Clear contact form
          name.value = "";
          subject.value = "";
          email.value = "";
          description.value = "";
        } else {
          alert("An error occurred while sending your email, Please try again");
        }
      } catch (error) {
        console.log(error);
      }
      return;
    }
    document.querySelector(
      "#contact-form-privacy-policy-error",
    ).innerText =
      "Before sending an email, please review and agree to our privacy policy";
  });
});
