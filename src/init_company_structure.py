#!/usr/bin/env python3
"""
xsvStudio Company Structure Builder - v2.0

RESTRUCTURED:
- Company folders at ROOT (not nested)
- Portfolio inside Marketing
- Templates moved to 04-TEMPLATES (Root Level)
- Added filtering logic for service templates

Author: xsvStudio Technology Division
Date: 2026-01-19
"""

import argparse
import os
import sys
from pathlib import Path

# Company structure (AT ROOT LEVEL)
COMPANY_STRUCTURE = {
    'HR': {
        'Policies': {},
        'Forms': {},
        'Employee-Records': {},
        'Benefits': {},
        'Onboarding': {}
    },
    'ACCOUNTING': {
        'Tax-Documents': {},
        'General-Ledger': {},
        'Financial-Reports': {},
        'Invoices': {},
        'Receipts': {}
    },
    'MARKETING': {
        'Brand-Assets': {},
        'Website-Content': {},
        'Social-Media': {},
        'Campaigns': {},
        'Analytics': {},
        'Portfolio': {
            'README.md': '# Portfolio & Case Studies\n\nPublished work for marketing and business development.',
            'Case-Studies': {},
            'Published-Work': {},
            'Client-Testimonials': {},
            'Award-Submissions': {}
        }
    },
    'OPERATIONS': {
        'SOP-Library': {},
        'Insurance': {},
        'Licenses': {},
        'Vendor-Contracts': {},
        'Equipment': {}
    },
    'BRANDING': {
        'Logos': {},
        'Color-Standards': {},
        'Typography': {},
        'Templates': {}
    },
    'CORPORATE-DOCS': {
        'Legal-Filings': {},
        'Contracts': {},
        'NDAs': {},
        'Articles-of-Incorporation': {},
        'Bylaws': {}
    }
}

# Project structure
PROJECT_STRUCTURE = {
    '01-INTERNAL-LABS': {
        'README.md': '# Internal Labs\n\nxsvStudio\'s own projects and R&D work.'
    },
    '02-EXTERNAL-CLIENTS': {
        'README.md': '# External Clients\n\nPaying customer projects organized by Client ID.\n\nStructure:\n- C-001-ClientName/\n  - CLIENT-MASTER-INDEX.md\n  - PROJECTS/\n  - 00-Client-Info/'
    },
    '03-PROPOSALS-PIPELINE': {
        'README.md': '# Proposals Pipeline\n\nActive proposals not yet converted to projects.',
        '2026': {},
        '2025-ARCHIVE': {}
    },
    '04-TEMPLATES': {
        'README.md': '# Service Templates\n\nStandard folder structures for each service division.'
    },
    '05-COMPLETED': {
        'README.md': '# Completed Projects\n\nArchived projects by year.',
        '2026': {},
        '2025': {},
        '2024': {}
    },
    '06-ARCHIVE': {
        'README.md': '# Archive\n\nOld projects and historical records.',
        'Pre-2024': {}
    }
}

# Service templates
SERVICE_TEMPLATES = {
    'WEB-TEMPLATE': {
        '00-PROJECT-INDEX.md': '# Website Project Template\n\nComplete workflow for web development projects.',
        '01-Contract-Financials': {
            'Invoicing': {
                'Billing-Template.xlsx': '',
                'Payment-Tracking.xlsx': '',
                'Invoice-History.md': ''
            },
            'Contract-Documents': {},
            'Change-Orders': {}
        },
        '02-Design-Planning': {
            'Branding-Assets': {},
            'Wireframes': {},
            'Mockups': {},
            'Client-Approvals': {}
        },
        '03-Execution-Deliverables': {
            'GitHub-Repo-Link.md': '# GitHub\n\nRepo link here',
            'Deployment-Info.md': '# Deployment',
            'Testing-Results': {},
            'Launch-Checklist.md': ''
        },
        '04-Client-Communications': {
            'Meeting-Minutes': {
                'Meeting-Template.docx': '',
                'Meeting-Notes-Log.md': ''
            },
            'Email-Threads': {},
            'Weekly-Reports': {}
        },
        '05-Closeout': {
            'Training-Documentation.pdf': '',
            'Handoff-Checklist.md': '',
            'Final-Invoice.xlsx': ''
        }
    },
    'IT-TEMPLATE': {
        '00-PROJECT-INDEX.md': '# IT Project Template',
        '01-Contract-Financials': {
            'Invoicing': {
                'Billing-Template.xlsx': '',
                'Payment-Tracking.xlsx': ''
            }
        },
        '02-Design-Planning': {
            'Migration-Plan.xlsx': '',
            'Network-Diagrams': {}
        },
        '03-Execution-Deliverables': {
            'Configuration-Scripts': {},
            'Testing-Results': {},
            'Labor-Tracking': {
                'Timesheet-Template.xlsx': '',
                'Labor-Cost-Report.xlsx': ''
            }
        },
        '04-Client-Communications': {
            'Meeting-Minutes': {
                'Meeting-Template.docx': ''
            }
        },
        '05-Closeout': {}
    },
    'CM-TEMPLATE': {
        '00-PROJECT-INDEX.md': '# Construction Management Template',
        '01-Contract-Financials': {
            'Invoicing': {
                'Billing-Template.xlsx': '',
                'Payment-Tracking.xlsx': '',
                'Subcontractor-Billing.xlsx': ''
            },
            'Change-Orders': {},
            'Pay-Applications': {},
            'Cost-Control': {
                'Budget-Tracker.xlsx': '',
                'Cost-Variance-Report.xlsx': '',
                'Committed-Cost-Log.xlsx': ''
            }
        },
        '02-Design-Planning': {
            'Construction-Drawings': {},
            'Master-Schedule.xlsx': '',
            'Permit-Applications': {}
        },
        '03-Execution-Deliverables': {
            'Daily-Reports': {},
            'RFIs': {},
            'Submittals': {},
            'Progress-Photos': {},
            'Labor-Tracking': {
                'Timesheet-Template.xlsx': '',
                'Labor-Cost-Report.xlsx': '',
                'Crew-Productivity.xlsx': ''
            },
            'Schedule': {
                'Master-Schedule.xlsx': '',
                'Milestone-Tracker.xlsx': '',
                '3-Week-Look-Ahead.xlsx': ''
            }
        },
        '04-Client-Communications': {
            'Meeting-Minutes': {
                'Meeting-Template.docx': '',
                'OAC-Meeting-Log.md': ''
            },
            'Weekly-Reports': {},
            'Owner-Correspondence': {}
        },
        '05-Closeout': {
            'Punch-List.xlsx': '',
            'Final-As-Builts': {},
            'Warranties': {},
            'Lien-Releases': {}
        }
    },
    'MFG-TEMPLATE': {
        '00-PROJECT-INDEX.md': '# Manufacturing Project Template',
        '01-Contract-Financials': {
            'Invoicing': {
                'Billing-Template.xlsx': '',
                'Payment-Tracking.xlsx': ''
            },
            'Cost-Control': {
                'Budget-Tracker.xlsx': '',
                'Material-Cost-Tracking.xlsx': ''
            }
        },
        '02-Design-Planning': {
            'Process-Flows': {},
            'CAD-Files': {},
            'BOM.xlsx': ''
        },
        '03-Execution-Deliverables': {
            'GMP-Compliance-Docs': {},
            'Test-Results': {},
            'Quality-Control-Reports': {}
        },
        '04-Client-Communications': {
            'Meeting-Minutes': {
                'Meeting-Template.docx': ''
            }
        },
        '05-Closeout': {}
    },
    'TECH-TEMPLATE': {
        '00-PROJECT-INDEX.md': '# Technology Project Template',
        '01-Contract-Financials': {
            'Invoicing': {
                'Billing-Template.xlsx': '',
                'Payment-Tracking.xlsx': ''
            }
        },
        '02-Design-Planning': {
            'System-Architecture': {},
            'API-Specifications': {},
            'Requirements-Doc.md': ''
        },
        '03-Execution-Deliverables': {
            'Source-Code-Link.md': '',
            'API-Documentation': {},
            'Testing-Reports': {}
        },
        '04-Client-Communications': {
            'Meeting-Minutes': {
                'Meeting-Template.docx': ''
            }
        },
        '05-Closeout': {}
    },
    'LEGAL-TEMPLATE': {
        '00-PROJECT-INDEX.md': '# Legal Services Template',
        '01-Contract-Financials': {
            'Invoicing': {
                'Billing-Template.xlsx': '',
                'Payment-Tracking.xlsx': ''
            }
        },
        '02-Design-Planning': {
            'Analysis-Strategy.md': ''
        },
        '03-Execution-Deliverables': {
            'Original-Contract.pdf': '',
            'Redlined-Version.pdf': ''
        },
        '04-Client-Communications': {
            'Meeting-Minutes': {
                'Meeting-Template.docx': ''
            }
        },
        '05-Closeout': {}
    },
    'MS-TEMPLATE': {
        '00-PROJECT-INDEX.md': '# Microsoft Solutions Template',
        '01-Contract-Financials': {
            'Invoicing': {
                'Billing-Template.xlsx': '',
                'Payment-Tracking.xlsx': ''
            }
        },
        '02-Design-Planning': {
            'Requirements-Gathering': {},
            'Solution-Design': {}
        },
        '03-Execution-Deliverables': {
            'Azure-Configurations': {},
            'Power-Apps-Solutions': {}
        },
        '04-Client-Communications': {
            'Meeting-Minutes': {
                'Meeting-Template.docx': ''
            }
        },
        '05-Closeout': {}
    },
    'MULTI-TEMPLATE': {
        '00-PROJECT-INDEX.md': '# Multi-Service Project Template',
        '01-Contract-Financials': {
            'Invoicing': {
                'Billing-Template.xlsx': '',
                'Payment-Tracking.xlsx': ''
            },
            'Cost-Control': {
                'Budget-Tracker.xlsx': '',
                'Cost-Variance-Report.xlsx': ''
            }
        },
        'WEB-Stream': {'README.md': '# Copy from WEB-TEMPLATE'},
        'IT-Stream': {'README.md': '# Copy from IT-TEMPLATE'},
        'CM-Stream': {'README.md': '# Copy from CM-TEMPLATE'},
        'SHARED': {
            'Master-Timeline.xlsx': '',
            'Unified-Invoicing': {},
            'Meeting-Minutes': {
                'Meeting-Template.docx': ''
            }
        }
    }
}

# Example client structure
EXAMPLE_CLIENT = {
    'C-001-ExampleClient': {
        'CLIENT-MASTER-INDEX.md': '''# Example Client

**Client ID:** C-001
**Company Name:** Example Corporation
**Primary Contact:** John Smith
**Email:** john@example.com
**Phone:** (555) 123-4567

## Active Projects
- None yet

## Completed Projects
- None yet

## Notes
This is an example client folder showing proper structure.
''',
        '00-Client-Info': {
            'Contact-Details.md': '',
            'Service-Agreement.pdf': '',
            'Insurance-Certificates': {}
        },
        'PROJECTS': {
            'README.md': '# Projects\n\nActive projects for this client.\n\nNaming: P-001-ProjectName-ServiceCode/'
        },
        'PROPOSALS': {
            'README.md': '# Proposals\n\nProposals for this client.'
        }
    }
}

class CompanyStructureBuilder:
    def __init__(self, root_path, local_mode=False):
        self.root_path = Path(root_path)
        self.local_mode = local_mode
        self.created_count = 0
        
    def create_structure(self, structure, parent_path):
        for name, content in structure.items():
            current_path = parent_path / name
            
            if isinstance(content, dict):
                self.create_folder(current_path)
                if content:
                    self.create_structure(content, current_path)
            elif isinstance(content, str):
                self.create_file(current_path, content)
    
    def create_folder(self, path):
        if self.local_mode:
            path.mkdir(parents=True, exist_ok=True)
        self.created_count += 1
    
    def create_file(self, path, content):
        if self.local_mode:
            path.parent.mkdir(parents=True, exist_ok=True)
            if content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                path.touch()
        self.created_count += 1
    
    def build_complete_structure(self, selected_services=None):
        self.create_folder(self.root_path)
        self.create_structure(COMPANY_STRUCTURE, self.root_path)
        self.create_structure(PROJECT_STRUCTURE, self.root_path)
        
        templates_path = self.root_path / '04-TEMPLATES'
        self.create_folder(templates_path)
        
        for service_name, service_structure in SERVICE_TEMPLATES.items():
            service_code = service_name.split('-')[0]
            if selected_services is None or service_code in selected_services:
                self.create_structure({service_name: service_structure}, templates_path)
        
        self.create_structure(EXAMPLE_CLIENT, self.root_path / '02-EXTERNAL-CLIENTS')
        self.create_master_docs()
    
    def create_master_docs(self):
        proposal_tracker = """# Proposal Tracker

Date,Client,Service,Description,Amount,Status
2026-01-19,Example Client,WEB,Portfolio Website,$5000,Pending
"""
        self.create_file(self.root_path / '03-PROPOSALS-PIPELINE' / 'PROPOSAL-TRACKER.md', proposal_tracker)
        
        service_codes = """# Service Codes

| Code | Division |
|------|----------|
| WEB | Website Development |
| IT | IT Services |
| CM | Construction Management |
| MFG | Manufacturing |
| TECH | Technology Solutions |
| LEGAL | Legal Services |
| MS | Microsoft Solutions |
| MULTI | Multi-Service Projects |
"""
        self.create_file(self.root_path / '04-TEMPLATES' / 'SERVICE-CODES.md', service_codes)

def main():
    parser = argparse.ArgumentParser(description='Build xsvStudio structure')
    parser.add_argument('--root', required=True, help='Root path')
    parser.add_argument('--local', action='store_true', help='Local filesystem mode')
    args = parser.parse_args()
    
    print(f"Creating structure at: {args.root}")
    response = input("Proceed? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Aborted.")
        return
    
    builder = CompanyStructureBuilder(args.root, args.local)
    builder.build_complete_structure()
    print(f"\n✅ Created {builder.created_count} items!")
    print(f"Location: {Path(args.root).absolute()}")

if __name__ == '__main__':
    main()
