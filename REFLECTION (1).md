# Reflection: Challenges in Translating Requirements to Use Cases & Tests

## 1. Difficulty in Mapping Complex Requirements

A major challenge I faced was breaking down complex security requirements into simple, actionable use cases. Integrating the SIEM system, for example, required detailed scenarios to ensure logs were processed and alerts managed properly. The complexity lay in handling various failure conditions and ensuring the system responded to each appropriately. Mapping this broad requirement into discrete steps for testing highlighted the need for thorough planning.

## 2. Balancing Security vs Usability

Balancing security measures, such as multi-factor authentication (MFA), with user accessibility was another challenge. While MFA enhances security, it can create friction for non-admin users. We addressed this by allowing non-admin users to opt out of MFA under specific conditions. This compromise required careful reflection in the use cases and test cases, ensuring that security wasn’t compromised while maintaining ease of access for users. This experience highlighted the importance of finding a middle ground in security-critical environments.

## 3. Writing Comprehensive Test Cases

Writing comprehensive test cases to cover all system functionalities proved challenging. The system had multiple actors, such as analysts, SOC managers, and end users, each with different actions. I approached the task by categorizing test cases into functional and non-functional types. Functional tests ensured the system performed tasks like incident logging and report generation correctly, while non-functional tests evaluated the system's scalability and encryption. This structured approach was key in ensuring the system's robustness but required several iterations to ensure complete coverage.

## 4. Performance Considerations

Another key challenge was ensuring the system could handle high user volumes during critical incidents. I simulated 1,000 users logging in concurrently to test system scalability. This test revealed performance bottlenecks, such as delays in processing logs and handling simultaneous authentication requests. The insights gained were invaluable in optimizing system performance, emphasizing the importance of stress testing systems in cybersecurity environments where performance and responsiveness are crucial.

## 5. Lessons Learned

A critical lesson from this process was the value of use case diagrams. They helped visualize the system’s interactions, making it easier to spot potential gaps or conflicts in the requirements. Another important takeaway was the importance of writing detailed acceptance criteria. These criteria ensured better test coverage and more precise validation of system behavior. It reinforced the need for clear, unambiguous requirements, especially in cybersecurity projects where precision is essential. 

Finally, communication with stakeholders played a key role in translating high-level requirements into testable components. Iterating on requirements with security analysts, IT admins, and end users helped ensure the system met both security and usability needs. The process taught me that careful planning, structured thinking, and collaboration are key to translating complex requirements into effective test cases.


