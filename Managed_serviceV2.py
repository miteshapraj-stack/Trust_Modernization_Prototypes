import sys
import os
from weasyprint import HTML

def generate_premium_managed_services_proposal():
    # 1. Get the absolute path of the folder where this script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Define the logo name
    logo_filename = "Credence logo.png"
    logo_path = os.path.join(script_dir, logo_filename)

    # 3. Check if the file actually exists before trying to run
    if not os.path.exists(logo_path):
        print(f"--- ERROR ---")
        print(f"Logo not found at: {logo_path}")
        print(f"Please ensure '{logo_filename}' is in the same folder as this script.")
        return

    print(f"Executing in Python Version: {sys.version}")
    print(f"Logo found at: {logo_path}")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{ size: A4; margin: 15mm; }}
            body {{ font-family: 'Segoe UI', Arial, sans-serif; color: #2c3e50; line-height: 1.5; font-size: 9.5pt; }}
            
            .header {{ 
                position: relative; 
                border-bottom: 3px solid #003366; 
                margin-bottom: 20px; 
                padding-bottom: 15px; 
                min-height: 75px; 
            }}
            
            .logo {{
                position: absolute;
                top: 0;
                right: 0;
                height: 55px;
                width: auto;
            }}

            h1 {{ color: #003366; font-size: 22pt; margin: 0; text-transform: uppercase; width: 75%; letter-spacing: 0.5px; }}
            .subtitle {{ font-size: 11pt; color: #7f8c8d; margin-top: 5px; font-weight: bold; }}
            h2 {{ color: #003366; border-bottom: 2px solid #ecf0f1; margin-top: 22px; font-size: 14pt; padding-bottom: 5px; text-transform: uppercase; page-break-after: avoid; }}
            h3 {{ color: #34495e; font-size: 11pt; margin: 12px 0 6px 0; background-color: #f4f6f7; padding: 6px 10px; border-left: 4px solid #003366; page-break-after: avoid; }}
            
            p {{ margin-bottom: 10px; text-align: justify; }}
            ul {{ margin-top: 5px; padding-left: 25px; margin-bottom: 15px; }}
            li {{ margin-bottom: 6px; text-align: justify; }}
            
            .table-container {{ margin-top: 15px; margin-bottom: 15px; page-break-inside: avoid; }}
            table {{ width: 100%; border-collapse: collapse; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
            th {{ background: #003366; color: white; padding: 10px; text-align: left; font-size: 9.5pt; text-transform: uppercase; }}
            td {{ border: 1px solid #bdc3c7; padding: 10px; font-size: 9.5pt; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            
            .note {{ background: #fdf2f2; border-left: 5px solid #e74c3c; padding: 12px; font-style: italic; margin: 15px 0; font-size: 9pt; color: #c0392b; page-break-inside: avoid; }}
            .highlight {{ font-weight: 600; color: #003366; }}
        </style>
    </head>
    <body>
        <div class="header">
            <img src="file:///{logo_path.replace('\\', '/')}" alt="Credence Logo" class="logo">
            <h1>Comprehensive Managed Services Operational Support</h1>
            <div class="subtitle">Strategic Operational Support & Value Delivery Framework</div>
        </div>

        <h2>Executive Summary</h2>
        <p>The objective of our managed services support is to transition your operations to a structured, outcome-based framework. We focus relentlessly on operational stability, data integrity, and strict SLA adherence. Through our proactive support model and continuous improvement approach, we aim to eliminate systemic issues before they arise. This framework operates as a strategic partnership, providing the leadership and engineering teams with actionable insights, predictable service models, and compelling long-term value.</p>

        <h2>Scope of Services</h2>
        
        <h3>Daily Operational Support</h3>
        <p>Our daily operations function as the backbone of your system, ensuring stronger data integrity and optimal audit readiness.</p>
        <ul>
            <li><span class="highlight">Trade Life Cycle Management:</span> We manage the end-to-end processing of trades, covering deal entry, system-level authorization, and settlement workflows. We ensure every action adheres strictly to your internal authorization matrix and regulatory audit requirements.</li>
            <li><span class="highlight">Financial Batch & Valuation Execution:</span> We execute the daily calculation of interest accruals and amortization/accretion schedules. We oversee portfolio updates through rigorous Mark-to-Market (MTM) valuation processes to maintain improved operational control.</li>
            <li><span class="highlight">Wealth & Security Management:</span> We support security-level events, including the posting of interest and corporate actions. We oversee the complex lifecycle of unit holder requests, ensuring seamless order allocation and final settlement.</li>
            <li><span class="highlight">NAV & Accounting Precision:</span> We support in the generation and authorization of daily accounting entries, which culminates in the precise daily generation of Net Asset Value (NAV) and Assets Under Management (AUM).</li>
            <li><span class="highlight">Reconciliation & Alignment:</span> We execute daily reconciliations across trades, accounting entries, and units, actively monitoring the daily movement of AUM and NAV to resolve anomalies immediately. Daily stand-ups guarantee there are no unexpected escalations, ensuring a predictable support model.</li>
        </ul>
        <div class="note">
            <strong>Mandatory Protocol:</strong> Execution of any trade lifecycle or process will be carried out only after obtaining approval from the Audit team.
        </div>

        <h3>Incident & Support Management</h3>
        <p>Our incident response is designed for faster issue resolution and reduced downtime.</p>
        <ul>
            <li>We monitor Application server health and triage alerts within defined SLA windows.</li>
            <li>We execute the rapid resolution of L1/L2 tickets daily, maintaining improved user confidence and a target system uptime of >99.5%.</li>
        </ul>

        <h3>Weekly / Monthly Governance Activities</h3>
        <p>We shift the focus from reactive response to proactive management.</p>
        <ul>
            <li><span class="highlight">Weekly Proactive Maintenance:</span> We manage scheduled preventive maintenance, ensuring security updates and validated backup procedures. We document new resolutions to reduce "tribal knowledge" dependency.</li>
            <li><span class="highlight">Monthly Executive Reporting:</span> We deliver consolidated executive reporting featuring month-over-month trend analysis against ticket volumes raised versus tickets resolved.</li>
            <li><span class="highlight">Monthly Problem Solving (RCA):</span> We execute comprehensive Root Cause Analysis (RCA) for all P1/P2 incidents. By identifying permanent fixes, we target an incident recurrence rate of &lt; 10%.</li>
        </ul>

        <h2>Support Coverage Window</h2>
        <div class="table-container">
            <table>
                <thead><tr><th>Coverage Type</th><th>Timing / Details</th></tr></thead>
                <tbody>
                    <tr><td><strong>Business Support</strong></td><td>9:00 AM – 6:00 PM IST</td></tr>
                    <tr><td><strong>P1/P2 Incident Support</strong></td><td>Extended Hours</td></tr>
                    <tr><td><strong>Weekend Support</strong></td><td>On Request / As Agreed</td></tr>
                </tbody>
            </table>
        </div>

        <h2>Governance Framework</h2>
        <div class="table-container">
            <table>
                <thead><tr><th>Meeting Type</th><th>Frequency</th><th>Objective</th></tr></thead>
                <tbody>
                    <tr><td><strong>Daily Ops Sync</strong></td><td>Daily</td><td>Align on daily priorities, risks, and blockers.</td></tr>
                    <tr><td><strong>Weekly Service Review</strong></td><td>Weekly</td><td>Review ticket trends and SLA compliance.</td></tr>
                    <tr><td><strong>Monthly Governance Review</strong></td><td>Monthly</td><td>Strategic reporting, RCA review, and ROI analysis.</td></tr>
                </tbody>
            </table>
        </div>

        <h2>KPI / SLA Metrics</h2>
        <div class="table-container">
            <table>
                <thead><tr><th>Measure</th><th>Target Goal</th><th>Strategic Value Delivered</th></tr></thead>
                <tbody>
                    <tr><td><strong>System Uptime</strong></td><td>99.5%</td><td>Continuous stability and availability.</td></tr>
                    <tr><td><strong>SLA Compliance</strong></td><td>&gt; 95%</td><td>Predictable, high-speed resolution of issues.</td></tr>
                    <tr><td><strong>MTTR (P1/P2)</strong></td><td>&lt; 4/8 Hours</td><td>Rapid recovery from critical business blockers.</td></tr>
                    <tr><td><strong>First Response Time</strong></td><td>&lt; 30 mins</td><td>Immediate acknowledgment and prioritization.</td></tr>
                    <tr><td><strong>Change Success Rate</strong></td><td>&gt; 95%</td><td>Safe, audited deployment of system changes.</td></tr>
                    <tr><td><strong>User Satisfaction Score</strong></td><td>&gt; 4/5</td><td>Stronger user confidence and adoption.</td></tr>
                    <tr><td><strong>CI Delivery</strong></td><td>1-2 per Month</td><td>Measurable uplift in system quality every month.</td></tr>
                </tbody>
            </table>
        </div>

        <h2>Roles & Responsibilities</h2>
        <ul>
            <li><strong>Managed Services Team:</strong> We execute daily operations, incident resolution, reporting, and continuous improvement initiatives.</li>
            <li><strong>Client Leadership/Audit:</strong> Provide strategic direction, regulatory advisory, and mandatory execution approvals.</li>
        </ul>

        <h2>Out of Scope / Assumptions</h2>
        <p>To ensure focused delivery, the following items remain outside the boundaries of this Managed Services agreement:</p>
        <ul>
            <li>New system enhancements or change requests.</li>
            <li>Major product customization or architectural rewrites.</li>
            <li>Delays caused directly by third-party vendors.</li>
        </ul>

        <h2>Value Proposition / Why Us</h2>
        <p>By engaging our Managed Services team, your organization benefits from a predictable support model and enhanced operational control. We act as an extension of your engineering team, contributing to the product roadmap from a deep operational lens. We deliver not just issue resolution, but proactive risk reduction, ensuring that your platform evolves seamlessly alongside your business needs.</p>

        <h2>Conclusion</h2>
        <p>This framework guarantees absolute transparency, unmatched data integrity, and dedicated strategic partnership. We look forward to driving your operational excellence forward.</p>

    </body>
    </html>
    """

    output_filename = "Premium_Executive_Managed_Services_Proposal.pdf"
    
    try:
        HTML(string=html_content).write_pdf(output_filename)
        print(f"--- SUCCESS ---")
        print(f"Premium Executive Document generated: {output_filename}")
    except Exception as e:
        print(f"--- ERROR ---")
        print(f"Failed to generate PDF: {e}")

if __name__ == "__main__":
    generate_premium_managed_services_proposal()