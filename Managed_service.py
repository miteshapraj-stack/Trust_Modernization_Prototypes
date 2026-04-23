import sys
import os
from weasyprint import HTML

def generate_incident_report():
    # 1. Get the absolute path of the folder where this script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Define the logo name
    logo_filename = "Credence logo.png"
    logo_path = os.path.join(script_dir, logo_filename)

    # Note: We are no longer throwing an error if the logo doesn't exist,
    # to ensure the script generates the PDF even if the file is temporarily missing.
    logo_url = f"file:///{logo_path.replace('\\', '/')}" if os.path.exists(logo_path) else ""

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @page {{ 
            size: A4; 
            margin: 15mm 12mm; 
            background-color: #f4f7f9; 
        }}
        body {{ 
            font-family: 'Segoe UI', Arial, sans-serif; 
            color: #2c3e50; 
            line-height: 1.5; 
            font-size: 9.5pt; 
            background-color: #f4f7f9;
        }}
        
        .header {{ 
            position: relative; 
            border-bottom: 3px solid #1f4e78; 
            margin-bottom: 15px; 
            padding-bottom: 10px; 
            min-height: 70px; 
        }}
        
        .logo {{
            position: absolute;
            top: 0;
            right: 0;
            height: 60px;
            width: auto;
        }}

        h1 {{ color: #1f4e78; font-size: 18pt; margin: 0; text-transform: uppercase; width: 85%; }}
        h2 {{ color: #1f4e78; border-bottom: 1px solid #1f4e78; margin-top: 15px; font-size: 13pt; padding-bottom: 3px; page-break-after: avoid; }}
        h3 {{ color: #1f4e78; font-size: 10.5pt; margin: 15px 0 5px 0; background-color: #e2e8f0; padding: 6px 10px; page-break-after: avoid; border-left: 4px solid #1f4e78; border-radius: 0 4px 4px 0; }}
        ul {{ margin-top: 5px; padding-left: 20px; }}
        li {{ margin-bottom: 8px; }}
        
        .incident-meta {{ background: #ffffff; padding: 12px; border: 1px solid #cdd4dc; margin-bottom: 15px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: flex; justify-content: space-between; }}
        .meta-item {{ font-size: 10pt; }}
        .icon {{ margin-right: 6px; }}
        
        /* Flowchart CSS */
        .flow-container {{ margin: 15px 0; padding: 0 10px; }}
        .flow-node {{ background-color: #ffffff; border: 1px solid #cdd4dc; border-left: 5px solid #1f4e78; border-radius: 6px; padding: 10px 15px; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.05); page-break-inside: avoid; }}
        .flow-arrow {{ text-align: center; color: #1f4e78; font-weight: bold; font-size: 16pt; line-height: 1; margin: 5px 0; page-break-inside: avoid; }}
        .flow-header {{ color: #1f4e78; font-weight: bold; font-size: 10pt; margin-bottom: 4px; border-bottom: 1px solid #f4f7f9; padding-bottom: 4px; }}
        
    </style>
</head>
<body>
    <div class="header">
        <img src="{logo_url}" alt="" class="logo">
        <h1>Incident Report & Oversight Framework</h1>
        <p><strong>📅 Date of Report:</strong> April 22, 2026 | <strong>🏢 Fund:</strong> GPHA</p>
    </div>

    <div class="incident-meta">
        <div class="meta-item"><strong>🟢 Status:</strong> Resolved / Post-Incident Recovery</div>
        <div class="meta-item"><strong>🔴 Severity Level:</strong> Critical</div>
    </div>

    <h3><span class="icon">📋</span>1. Executive Summary</h3>
    <ul>
        <li><strong>Incident Overview:</strong> The user initially entered a MF-BUY transaction on 20th February 2025 and then wanted to reverse it. This sequence led the Stanbic team to execute a "REV-MF-BUY transaction" in the system on 05th March 2025, which was due for settlement on same day. Stanbic team did the settlement of this transaction on 12th March 2025 and also added a MF-BUY transaction of same amount.</li>
        <li><strong>Essence of the Incident:</strong> Fundamentally, this incident involved a MF-BUY reversal that was fully processed, followed immediately by an additional MF-BUY entry. The transaction amount for these entries was 98,584,044 GHS.</li>
        <li><strong>Impact:</strong> The execution of these transactions created a critical system misalignment in the units of the fund. This led to the artificial inflation of the GPHA fund's Net Asset Value (NAV), which remained undetected until client's reported concerns prompted a formal investigation.</li>
    </ul>

    <h3><span class="icon">🔍</span>2. Issue Identification & Resolution Action Taken</h3>
    <ul>
        <li><strong>February 09, 2026:</strong> A Journal Voucher (JV) was executed to align the valuation with the Trial Balance (TB). The Journal Voucher entry was passed by Stanbic team without taking any support from Credence regarding the correction of AUM by passing a JV.</li>
        <li><strong>February 16, 2026:</strong> The SIMS team logged Redmine ID #144543 regarding an inflated GPHA Net Asset Value (NAV) after the client reported concerns.</li>
        <li><strong>Underlying Root Cause Data:</strong> The user executed a (REV-MF-BUY) to correct a wrongly entered contribution on 20th February 2025. Because no accounting entry was set for REV-MF-BUY, no accounting entry was generated. This user's reversal did not changed the outstanding amount and also failed to change the units because they did not complete all the required processes, creating a misalignment. An additional contribution was then executed on 12th March 2025 to correct the initial mistake.</li>
        <li><strong>Correction Coordination:</strong> We corrected the GPHA NAV in coordination with the SIMS team. We requested access to the Production server to correct the transactions, and re-generate NAV for the past year from February 20, 2025 to February 22, 2026.</li>
        <li><strong>Completion:</strong> The SIMS team was kept informed and concurrently connected via Google Meet for every step taken. They were fully updated regarding the impact on NAV numbers and Withdrawal cases. The corrections and re-run for the entire year were completed by us on February 22, 2026.</li>
    </ul>

    <h3><span class="icon">⏱️</span>3. Operations Timeline of Events</h3>
    <div class="flow-container">
        
        <div class="flow-node">
            <div class="flow-header">📅 20 Feb 2025 | Initial Contribution</div>
            <div>A contribution of 98,584,044 GHS was formally entered.</div>
        </div>
        
        <div class="flow-arrow">↓</div>
        
        <div class="flow-node">
            <div class="flow-header">📅 05 Mar 2025 | Transaction Reversal</div>
            <div>The SIMS team executed the reversal using the transaction type REV-MF-BUY.</div>
        </div>
        
        <div class="flow-arrow">↓</div>
        
        <div class="flow-node">
            <div class="flow-header">📅 12 Mar 2025 | Settlement of REV-MF-BUY & Correct Contribution Entry</div>
            <div>The SIMS team "settled REV-MF-BUY on 12th March 2025 contribution" and "added additional entry" of 98,584,044 GHS without seeking guidance.</div>
        </div>
        
        <div class="flow-arrow">↓</div>
        
        <div class="flow-node">
            <div class="flow-header">⚙️ Post-Transaction | System Updates</div>
            <div>After the initial transaction dates (20th Feb 2025, 5th Mar 2025/12th Mar 2025), all processes were run, and the system updated. The user could have avoided this incident by settling and checking the accounting entry the first time they entered the reverse buy to see what updates had occurred.</div>
        </div>
        
        <div class="flow-arrow">↓</div>
        
        <div class="flow-node">
            <div class="flow-header">📅 12 Mar to 16 Feb 2026 | Client Reported Concerns</div>
            <div>The client reported concerns to the SIMS team regarding inconsistencies where their balances did not align with withdrawal positions.</div>
        </div>
        
        <div class="flow-arrow">↓</div>
        
        <div class="flow-node">
            <div class="flow-header">📅 16 Feb 2026 | Issue Escalated to Credence</div>
            <div>The SIMS team reported the issue on the Redmine portal (Ticket #144543).</div>
        </div>
        
        <div class="flow-arrow">↓</div>
        
        <div class="flow-node" style="border-left-color: #e63946;">
            <div class="flow-header" style="color: #e63946;">📅 18 Feb 2026 | Root Cause Identified</div>
            <div>Technical investigation confirmed the inflation was caused by the transaction combinations and the failure to verify AUM impacts.</div>
        </div>
        
    </div>

    <h3><span class="icon">📉</span>4. Business Impact</h3>
    <ul>
        <li><strong>Duration of Impact:</strong> February 22, 2025 - February 18, 2026</li>
        <li><strong>Areas Affected:</strong> GPHA Fund NAV, AUM Calculations, Client Payouts</li>
        <li><strong>Financial Impact:</strong> Artificial AUM inflation of 98,584,044 GHS, which resulted in an overpayment to the client. Client also experienced negative balances on Consolidated PF statements.</li>
    </ul>

    <h3><span class="icon">🧩</span>5. Root Cause Analysis (RCA)</h3>
    <ul>
        <li><strong>Accounting Configuration Issue:</strong> The system environment was originally configured in December 2018. The accounting entry configuration for this specific reverse mutual fund buy transaction was missed due to an oversight by both the users and the implementation team at that time. This missing configuration is exactly why no accounting entry was generated.</li>
        <li><strong>System Version:</strong> The existing system version currently in use is from 2018. The new version of our system includes built-in validations that would have automatically prevented this configuration issue.</li>
        <li><strong>Unit Misalignment:</strong> The user's reversal did not change the outstanding amount and also failed to change the units because they did not complete all the required processes. This incomplete action created the misalignment between the NAV and the units.</li>
        <li><strong>User Error & Avoidance:</strong> The user executed REV-MF-BUY on 05th Mar 2025 in intend to reverse the MF-BUY executed on 20th Feb 2025 and was due for settlement on 05th Mar 2025, which was then settled on 12th Mar 2025 with additional MF-BUY without seeking guidance. They could have easily avoided the issue if they had consulted Credence prior to processing the duplicate transaction.</li>
    </ul>

    <h3><span class="icon">🛡️</span>6. Resolution & Preventative Measures</h3>
    <p>To ensure this type of operational oversight and system error does not occur again, strict technical and procedural safeguards are being implemented.</p>
    <p><strong>☑ Immediate Resolution:</strong></p>
    <ul>
        <li>The NAV of the GPHA fund has been manually corrected in coordination with the SIMS team.</li>
        <li>The REV-MF-BUY, REV-MF-SELL transaction type has been fully configured with the correct accounting entries to ensure future reversals accurately impact the AUM.</li>
    </ul>
    <p><strong>🚧 Preventative Measures:</strong></p>
    <ul>
        <li><strong>Mandatory Post-Transaction Verification (Process Update):</strong> The SIMS team's Standard Operating Procedures (SOPs) must be updated to mandate a "maker-checker" review or manual AUM validation immediately following any manual reversal, adjustment, or high-value entry.</li>
        <li><strong>Unmapped Transaction Blocks (System Update):</strong> Implemented the accounting entries for REV-MF-BUY and REV-MF-SELL voucher to avoid such cases in the near future.</li>
        <li><strong>System Configuration & Upgrade Enablement:</strong> Necessary configuration controls have been strengthened to ensure proper usage of transaction types, and upcoming future system upgrades will further enhance functionality coverage, reducing dependency on manual validation and supporting more consistent transaction processing.</li>
    </ul>

    <h3><span class="icon">🔭</span>7. Future-State NAV Monitoring & Proactive Oversight Framework</h3>
    <p>Within a managed services construct, a dedicated resource implements a well-defined and continuous oversight framework for monitoring NAV movement patterns, complemented by both periodic and exception-based reviews of NAV extract reports. This includes:</p>
    <ul>
        <li>Ongoing monitoring of NAV movement patterns supported by defined thresholds.</li>
        <li>Periodic and exception-based reviews of NAV extract reports.</li>
        <li>Structured variance analysis and trend tracking across defined time intervals.</li>
        <li>Validation of key data points to ensure consistency and reporting integrity.</li>
    </ul>
    <p>Such an approach naturally enhances early visibility into evolving patterns, allowing incremental deviations to be identified in a timely and measured manner. These observations are generally supported by initial contextual assessments, helping to distinguish between expected market-driven movements and potential underlying variances. In effect, this model enables a more proactive and seamlessly governed escalation process, ensuring that relevant stakeholders are engaged with the right insights at the right time, thereby supporting informed, timely, and well-controlled corrective actions where required.</p>

</body>
</html>"""
    
    output_filename = "GPHA_Incident_Report_Final.pdf"
    
    try:
        HTML(string=html_content).write_pdf(output_filename)
        print(f"--- SUCCESS ---")
        print(f"Document generated successfully: {output_filename}")
    except Exception as e:
        print(f"--- ERROR ---")
        print(f"Failed to generate PDF: {e}")

if __name__ == "__main__":
    generate_incident_report()