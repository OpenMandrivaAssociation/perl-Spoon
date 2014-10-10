%define module	Spoon

%if %{_use_internal_dependency_generator}
%define __noautoprov 'perl\\(IO::All\\)'
%else
%define _provides_exceptions perl(IO::All)
%endif

Name:		perl-%{module}
Version:	0.24
Release:	7
Summary:	A Spiffy Application Building Framework 
URL:		http://search.cpan.org/dist/%{module}
# no available category
Source:		http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{module}-%{version}.tar.gz
License:	GPL
Group:		Development/Perl
BuildRequires:	perl-devel
BuildRequires:	perl(IO::All)
BuildRequires:	perl(CGI)
BuildRequires:	perl(DB_File)
BuildRequires:	perl(Template)
BuildRequires:	perl(Spiffy)
BuildRequires:	perl(URI::Escape)
BuildArch:	noarch

%description
Spoon is an Application Framework that is designed primarily for building
Social Software web applications. The Kwiki wiki software is built on top of
Spoon.

Spoon::Base is the primary base class for all the Spoon::* modules. Spoon.pm
inherits from Spiffy.pm.

Spoon is not an application in and of itself. (As compared to Kwiki) You need
to build your own applications from it.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Spoon
%{perl_vendorlib}/Spoon.pm
%{_mandir}/*/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.24-5mdv2010.0
+ Revision: 430542
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.24-4mdv2009.0
+ Revision: 258358
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.24-3mdv2009.0
+ Revision: 246422
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.24-1mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2008.0
+ Revision: 48176
- new version


* Fri Jun 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-4mdv2007.0
- buildrequires perl(URI::Escape)

* Fri Jun 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-3mdv2007.0
- buildrequires Perl(Spiffy)

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.23-2mdk
- Rebuild

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdk 
- first mandriva release

