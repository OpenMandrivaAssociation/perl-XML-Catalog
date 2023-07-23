%define module XML-Catalog
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	1.03
Release:	1
Summary:	Resolve public identifiers and remap system identifiers
URL:		https://metacpan.org/pod/XML::Catalog
Source:		https://cpan.org/modules/by-module/XML/%{module}-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(LWP::Simple)
BuildArch:	noarch

%description
This module implements draft 0.4 of John Cowan's XML Catalog proposal.
Catalogs may be written in either SOCAT or XML syntax (see the proposal
for syntax details); XML::Catalog will assume SOCAT syntax if the
catalog is not in well-formed XML syntax.

This module, as of 1.0.0, also supports Oasis XML catalogs.

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*
