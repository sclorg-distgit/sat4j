%{?scl:%scl_package sat4j}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

# should be consistent across one release
%global build_date 20130405

Name:           %{?scl_prefix}sat4j
Version:        2.3.5
Release:        8.%{baserelease}%{?dist}
Summary:        A library of SAT solvers written in Java

License:        EPL or LGPLv2
URL:            http://www.sat4j.org/
# Created by sh sat4j-fetch.sh
Source0:        sat4j-%{version}.tar.xz
Source1:        sat4j-fetch.sh
Patch0:         sat4j-classpath.patch

BuildRequires:  %{?scl_prefix_java_common}ant
BuildRequires:  %{?scl_prefix_maven}javapackages-local
Requires:       %{?scl_prefix_java_common}javapackages-tools

BuildArch:      noarch

%description
The aim of the SAT4J library is to provide an efficient library of SAT
solvers in Java. The SAT4J library targets first users of SAT "black
boxes", those willing to embed SAT technologies into their application
without worrying about the details.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n sat4j-%{version}
%patch0
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
ant -Dbuild.compiler=modern -Drelease=%{version} \
 -Dtarget=1.5 -DBUILD_DATE=%{build_date} p2 
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -rp dist/%{version}/org.sat4j.core.jar \
 $RPM_BUILD_ROOT%{_javadir}
cp -rp dist/%{version}/org.sat4j.pb.jar \
 $RPM_BUILD_ROOT%{_javadir}
%{?scl:EOF}


%files
# No %%doc files as the about.html is in the jar
%{_javadir}/org.sat4j*

%changelog
* Thu Jul 21 2016 Mat Booth <mat.booth@redhat.com> - 2.3.5-8.1
- Auto SCL-ise package for rh-eclipse46 collection

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.5-7
- Add build-requires on javapackages-local

* Mon Jun 22 2015 Mat Booth <mat.booth@redhat.com> - 2.3.5-6
- Remove SCL macros and tidy spec

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Alexander Kurtakov <akurtako@redhat.com> 2.3.5-3
- Remove useless parts.
- Require java-headless.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.5-1
- Update to latest upstream.

* Fri May 10 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.4-1
- Update to latest upstream.

* Wed Apr 17 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.3-7
- Remove jars from source.

* Fri Apr 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.0-6
- Update to 2.3.3
- Initial sclization.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Andrew Overholt <overholt@redhat.com> 2.3.0-2
- Make 1.5-level bytecode.  This enables bootstrapping of Eclipse
  with OpenJDK 7.

* Mon Apr 04 2011 Chris Aniszczyk <zx@redhat.com> 2.3.0-1
- Update to 2.3.0.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 8 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2.0-1
- Update to 2.2.0.

* Tue Mar 30 2010 Andrew Overholt <overholt@redhat.com> 2.1.1-3
- Fix license tag

* Fri Mar 26 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-2
- Switch to lzma tarball.
- Remove classpath in manifest.

* Sun Mar 7 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-1
- Update to 2.1.1.

* Tue Aug 4 2009 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-1
- Update to 2.1.0 final.

* Wed Apr 8 2009 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-0.1.rc2
- Update to 2.1.0.RC2.

* Thu Feb 26 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.3-1
- Update to 2.0.3.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-7
- eclipse_base is now libdir/eclipse

* Tue Jul 15 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-6
- Build with OpenJDK (java.util.Scanner)

* Tue Jul 15 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-5
- Use sed instead of dos2unix

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-4
- Remove jmock JARs
- Don't run tests as part of build

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-3
- Remove Class-Path from pb MANIFEST.MF

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-2
- Add eclipse-pde BR for pdebuild script

* Fri Jun 27 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-1
- 2.0.0
- Run tests

* Thu Mar 13 2008 Andrew Overholt <overholt@redhat.com> 2.0-0.1.RC5
- Initial version